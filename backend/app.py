import os
import platform
import asyncio
import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS
import aiofiles

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Compiler API!"

@app.route('/compile', methods=['POST'])
async def compile_code():
    data = request.get_json()
    code = data.get('code', '')
    user_input = data.get('input', '')

    # Write the code to a temporary file
    async with aiofiles.open('code.c', 'w') as code_file:
        await code_file.write(code)

    temp_input_file = 'input.txt'
    temp_output_file = 'output.txt'

    # Save user input to a file asynchronously
    async with aiofiles.open(temp_input_file, 'w') as input_file:
        await input_file.write(user_input)

    # Compile and run the code
    try:
        compile_command = ['gcc', 'code.c', '-o', 'code']
        compile_process = await asyncio.create_subprocess_exec(*compile_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        stderr, _ = await compile_process.communicate()

        if compile_process.returncode != 0:
            error_message = stderr.decode()
            formatted_error = format_error(error_message)
            return jsonify({'output': formatted_error}), 400

        # Run the executable with user input redirection
        exec_command = f'./code < {temp_input_file} > {temp_output_file}'
        exec_process = await asyncio.create_subprocess_shell(exec_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        await exec_process.communicate()

        async with aiofiles.open(temp_output_file, 'r') as output_file:
            output = await output_file.read()

        return jsonify({'output': output})

    except Exception as e:
        return jsonify({'output': f"An error occurred: {str(e)}"}), 500

def format_error(error_output):
    """
    This function formats the GCC error messages to be more beginner-friendly.
    """
    errors = error_output.splitlines()
    formatted_errors = []
    
    for error in errors:
        if 'error:' in error:
            error_line = error.split('error:')[0].strip()
            error_message = error.split('error:')[1].strip()
            line_info = error_line.split(':')
            line_number = line_info[1]  # Line number (e.g., '5')
            formatted_error = f"Error on Line {line_number}: {error_message}\n"
            
            if 'expected \';\'' in error_message:
                formatted_error += "Hint: It looks like you're missing a semicolon at the end of the statement.\n"
            
            formatted_errors.append(formatted_error)
        else:
            formatted_errors.append(error)

    return "\n".join(formatted_errors)

if __name__ == '__main__':
    # Use dynamic port for Render deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

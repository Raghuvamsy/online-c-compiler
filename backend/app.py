import subprocess
import os
import platform
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Compiler API!"

@app.route('/compile', methods=['POST'])
def compile_code():
    data = request.get_json()
    code = data.get('code', '')
    user_input = data.get('input', '')

    # Define temporary file names
    code_file = 'code.c'
    executable = 'code.exe' if platform.system() == 'Windows' else './code'
    input_file = 'input.txt'
    output_file = 'output.txt'

    try:
        # Write the C code to a file
        with open(code_file, 'w') as cf:
            cf.write(code)

        # Write user input to a file
        with open(input_file, 'w') as inf:
            inf.write(user_input)

        # Compile the C code
        compile_process = subprocess.run(['gcc', code_file, '-o', 'code'], stderr=subprocess.PIPE, text=True)

        if compile_process.returncode != 0:
            # Compilation error
            formatted_error = format_error(compile_process.stderr)
            return jsonify({'output': formatted_error}), 400

        # Execute the compiled program with user input
        exec_command = [executable]
        with open(input_file, 'r') as inf, open(output_file, 'w') as outf:
            exec_process = subprocess.run(exec_command, stdin=inf, stdout=outf, stderr=subprocess.PIPE, text=True)

        if exec_process.returncode != 0:
            # Runtime error
            return jsonify({'output': exec_process.stderr}), 400

        # Read the output from the execution
        with open(output_file, 'r') as outf:
            output = outf.read()

        return jsonify({'output': output})

    except Exception as e:
        return jsonify({'output': f"An error occurred: {str(e)}"}), 500

    finally:
        # Clean up temporary files
        for file in [code_file, 'code', input_file, output_file]:
            if os.path.exists(file):
                os.remove(file)

def format_error(error_output):
    """
    Formats GCC error messages to be more beginner-friendly.
    """
    errors = error_output.splitlines()
    formatted_errors = []

    for error in errors:
        if 'error:' in error:
            parts = error.split('error:')
            if len(parts) > 1:
                location = parts[0].strip()
                message = parts[1].strip()

                # Extract line number
                location_parts = location.split(':')
                line_number = location_parts[1] if len(location_parts) > 1 else "unknown"

                formatted_error = f"Error on Line {line_number}: {message}\n"

                # Add specific hints
                if "expected ';'" in message:
                    formatted_error += "Hint: It looks like you're missing a semicolon at the end of the statement.\n"

                formatted_errors.append(formatted_error)
            else:
                formatted_errors.append(error)
        else:
            formatted_errors.append(error)

    return "\n".join(formatted_errors)

if __name__ == '__main__':
    # Use dynamic port for Render deployment
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

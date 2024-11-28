import os
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

    # Write the code to a temporary file
    async with aiofiles.open('code.c', 'w') as code_file:
        await code_file.write(code)

    temp_output_file = 'output.txt'

    try:
        # Compile the code
        compile_command = ['gcc', 'code.c', '-o', 'code']
        compile_process = await asyncio.create_subprocess_exec(
            *compile_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE
        )
        stderr, _ = await compile_process.communicate()

        if compile_process.returncode != 0:
            error_message = stderr.decode()
            return jsonify({'output': error_message}), 400

        # Run the compiled program
        exec_command = './code'
        exec_process = await asyncio.create_subprocess_shell(
            exec_command,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        try:
            stdout, stderr = await asyncio.wait_for(exec_process.communicate(), timeout=10)
        except asyncio.TimeoutError:
            exec_process.kill()
            return jsonify({'output': 'Execution timed out!'}), 400

        # Handle program output and errors
        output = stdout.decode() if stdout else ''
        error_output = stderr.decode() if stderr else ''
        if error_output:
            return jsonify({'output': error_output}), 400

        return jsonify({'output': output.strip()})

    except Exception as e:
        return jsonify({'output': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

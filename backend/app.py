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

    # Save the code to a file
    with open('code.c', 'w') as code_file:
        code_file.write(code)

    try:
        # Compile the C program
        compile_result = subprocess.run(['gcc', 'code.c', '-o', 'code'], stderr=subprocess.PIPE, text=True)
        if compile_result.returncode != 0:
            return jsonify({'output': compile_result.stderr}), 400  # Compilation error

        # Run the compiled program and pass input dynamically
        executable = 'code.exe' if platform.system() == 'Windows' else './code'
        process = subprocess.Popen(
            executable,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Get user input and send to the executable
        user_input = data.get('input', '')  # Dynamically fetch user input
        output, errors = process.communicate(input=user_input)

        if process.returncode != 0:
            return jsonify({'output': errors or 'Runtime error occurred.'}), 400  # Runtime error

        return jsonify({'output': output})

    except Exception as e:
        return jsonify({'output': f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

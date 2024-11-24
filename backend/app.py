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

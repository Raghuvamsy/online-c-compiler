import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/compile', methods=['POST'])
def home():
    return "Welcome to the Compiler API!"
def compile_code():
    data = request.get_json()
    code = data.get('code', '')

    # Write the code to a temporary file
    with open('code.c', 'w') as code_file:
        code_file.write(code)

    # Compile the C code using gcc and capture the output/errors
    try:
        result = subprocess.run(['gcc', 'code.c', '-o', 'code'], stderr=subprocess.PIPE, text=True)
        
        if result.returncode != 0:
            # If there is an error, parse the error message
            error_output = result.stderr
            formatted_error = format_error(error_output)
            return jsonify({'output': formatted_error})
        else:
            # If compilation is successful, run the code and return output
            run_result = subprocess.run(['./code'], stdout=subprocess.PIPE, text=True)
            return jsonify({'output': run_result.stdout})
    
    except Exception as e:
        return jsonify({'output': f"An error occurred: {str(e)}"})

def format_error(error_output):
    """
    This function formats the GCC error messages to be more beginner-friendly.
    """
    errors = error_output.splitlines()
    formatted_errors = []
    
    for error in errors:
        if 'error:' in error:
            # Extract the error line and message
            error_line = error.split('error:')[0].strip()
            error_message = error.split('error:')[1].strip()
            
            # Extract line number and column from the error
            # Example: 'code.c:5:3:' means line 5, column 3
            line_info = error_line.split(':')
            line_number = line_info[1]  # Line number (e.g., '5')
            
            # Clean up the error message for beginners
            formatted_error = f"Error on Line {line_number}: {error_message}\n"
            
            # Add a suggestion for missing semicolons
            if 'expected \';\'' in error_message:
                formatted_error += "Hint: It looks like you're missing a semicolon at the end of the statement.\n"
            
            formatted_errors.append(formatted_error)
        else:
            formatted_errors.append(error)

    return "\n".join(formatted_errors)

if __name__ == '__main__':
    app.run(debug=True)

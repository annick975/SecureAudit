from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging to log errors to the console
logging.basicConfig(level=logging.DEBUG)

@app.route('/analyze', methods=['POST'])
def analyze_code():
    try:
        code = request.json.get('code')
        if not code:
            app.logger.error("No code provided")
            return jsonify({"error": "No code provided"}), 400  # Bad Request
        

        app.logger.debug(f"Received code for analysis: {code}")

        # Write the code to a temporary Python file for analysis
        with open('temp_code.py', 'w') as f:
            f.write(code)

        # Run Bandit to analyze the Python code
        result = subprocess.run(['bandit', '-r', 'temp_code.py'], capture_output=True, text=True)


        if result.returncode != 0:
            app.logger.error(f"Bandit error: {result.stderr}")
            return jsonify({"error": "Error running Bandit", "details": result.stderr}), 500

        # Return the output of Bandit
        output = result.stdout.splitlines()
        return jsonify({"results": output})  # This wraps the output in a JSON object


    except Exception as e:
        app.logger.error(f"Exception occurred: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

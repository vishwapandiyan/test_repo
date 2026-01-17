"""Sample Flask application with intentional security issues for testing."""

from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Hardcoded secrets - SECURITY ISSUE
API_KEY = "AKIAIOSFODNN7EXAMPLE"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz123456"
GOOGLE_API_KEY = "AIzaSyDummyGoogleAPIKeyForTestingPurposesOnly12345"

# Database connection - SECURITY ISSUE: hardcoded password
DB_PASSWORD = "super_secret_password_123"
database_url = f"postgresql://user:{DB_PASSWORD}@localhost/mydb"

@app.route('/login', methods=['POST'])
def login():
    """Login endpoint with potential SQL injection vulnerability."""
    username = request.form.get('username')
    password = request.form.get('password')
    
    # SECURITY ISSUE: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = psycopg2.connect(database_url)
    cursor = conn.cursor()
    cursor.execute(query)  # Dangerous!
    
    return jsonify({"status": "logged_in"})

@app.route('/config')
def get_config():
    """Expose configuration."""
    # SECURITY ISSUE: Exposing secrets in response
    return jsonify({
        "api_key": API_KEY,
        "db_password": DB_PASSWORD
    })

@app.route('/eval')
def eval_code():
    """Dangerous endpoint using eval."""
    code = request.args.get('code')
    # SECURITY ISSUE: Using eval with user input
    result = eval(code)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


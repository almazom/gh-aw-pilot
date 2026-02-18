"""
Sample application with security vulnerabilities for testing Code Reviewer Agent
"""
import hashlib
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Hardcoded credentials - SECURITY ISSUE
DATABASE_URL = "postgresql://admin:SuperSecret123@localhost:5432/production"
API_KEY = "sk-live-abc123xyz789"
AWS_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    user = cursor.fetchone()
    
    if user:
        return jsonify({"status": "success", "user_id": user[0]})
    return jsonify({"status": "failed"})

@app.route('/users/<user_id>')
def get_user(user_id):
    # No input validation
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Another SQL injection point
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    user = cursor.fetchone()
    
    # Exposing sensitive data
    return jsonify({
        "id": user[0],
        "username": user[1],
        "email": user[2],
        "password_hash": user[3],  # Should not expose password hash
        "ssn": user[4],  # Exposing SSN!
        "credit_card": user[5]  # Exposing credit card!
    })

@app.route('/hash_password', methods=['POST'])
def hash_password():
    password = request.form.get('password')
    
    # Weak hashing algorithm
    hashed = hashlib.md5(password.encode()).hexdigest()
    
    return jsonify({"hash": hashed})

@app.route('/execute', methods=['POST'])
def execute_command():
    import os
    cmd = request.form.get('command')
    
    # Command injection vulnerability
    result = os.system(cmd)
    
    return jsonify({"result": result})

@app.route('/data')
def get_all_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # N+1 query problem
    cursor.execute("SELECT id FROM users")
    user_ids = cursor.fetchall()
    
    results = []
    for uid in user_ids:
        cursor.execute(f"SELECT * FROM orders WHERE user_id = {uid[0]}")
        orders = cursor.fetchall()
        results.append({"user_id": uid[0], "orders": orders})
    
    return jsonify(results)

@app.errorhandler(500)
def handle_error(e):
    # Exposing stack traces
    import traceback
    return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

if __name__ == '__main__':
    # Debug mode enabled in production
    app.run(debug=True, host='0.0.0.0')

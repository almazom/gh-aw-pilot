import os

# Bad code for testing code reviewer

def login(username, password):
    # Hardcoded secret - security issue!
    SECRET_KEY = "super-secret-key-12345"
    
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE username = {username}"
    
    # No error handling
    result = execute_query(query)
    return result

def get_user_data(user_id):
    # N+1 query problem
    users = get_all_users()
    data = []
    for user in users:
        orders = get_orders(user.id)  # Query in loop!
        data.append(orders)
    return data

# Global variable - bad practice
cache = {}

def process_data(items):
    # No logging, no validation
    for item in items:
        dangerous_operation(item)


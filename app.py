import sqlite3
import os

def get_user_data(username):
    """
    Insecure coding practice: SQL Injection vulnerability.
    This will be flagged by Bandit.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Fix: Use parameterized query to prevent SQL Injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

def do_aws_stuff():
    """
    Hardcoded secret.
    This will be flagged by Secret Scanning tools (like Gitleaks).
    """
    # Fix: Retrieve secrets securely via environment variables
    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
    
    print("Connecting to AWS...")
    return True

if __name__ == "__main__":
    print("Running dummy app")

import sqlite3

def get_user_data(username):
    """
    Insecure coding practice: SQL Injection vulnerability.
    This will be flagged by Bandit.
    """
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Flaw: String formatting used to construct SQL query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()

def do_aws_stuff():
    """
    Hardcoded secret.
    This will be flagged by Secret Scanning tools (like Gitleaks).
    """
    # Flaw: Hardcoded AWS access keys
    aws_access_key_id = "AKIAIOSFODNN7EXAMPLE" 
    aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    
    print("Connecting to AWS...")
    return True

if __name__ == "__main__":
    print("Running dummy app")

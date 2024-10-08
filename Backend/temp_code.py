import os
import hashlib
import pickle
import sqlite3

# 1. Command Injection Vulnerability
def run_command(user_input):
    os.system(f"echo {user_input}")

# 2. Hardcoded Password
def check_password(input_password):
    hardcoded_password = "Pa$$w0rd123"
    if input_password == hardcoded_password:
        print("Access Granted")
    else:
        print("Access Denied")

# 3. Weak Cryptographic Hash (MD5)
def hash_data(data):
    return hashlib.md5(data.encode()).hexdigest()

# 4. Insecure Deserialization
def deserialize_data(serialized_data):
    return pickle.loads(serialized_data)

# 5. SQL Injection Vulnerability
def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def main():
    # Vulnerable command injection
    user_input = input("Enter a command: ")
    run_command(user_input)

    # Checking password with hardcoded value
    password = input("Enter password: ")
    check_password(password)

    # Weak hashing example
    data = input("Enter data to hash: ")
    print(f"MD5 Hash: {hash_data(data)}")

    # Insecure deserialization example
    serialized = pickle.dumps({"user": "admin"})
    deserialized = deserialize_data(serialized)
    print(f"Deserialized Data: {deserialized}")

    # SQL Injection vulnerability example
    username = input("Enter a username: ")
    user_data = get_user_data(username)
    print(f"User data: {user_data}")

if __name__ == "__main__":
    main()

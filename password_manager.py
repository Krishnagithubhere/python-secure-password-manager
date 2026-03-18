import json
import hashlib
import os

FILE = "passwords.json"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_data():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f)

def add_password():
    site = input("Enter site name: ")
    password = input("Enter password: ")
    
    data = load_data()
    data[site] = hash_password(password)
    save_data(data)
    
    print("Password saved securely!")

def view_passwords():
    data = load_data()
    if not data:
        print("No data found.")
        return
    
    for site in data:
        print(f"{site} -> {data[site]}")

def main():
    while True:
        print("\n1. Add Password")
        print("2. View Passwords")
        print("3. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
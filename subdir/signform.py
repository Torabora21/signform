def authenticate_user():
    # Prompt user for a password
    user_password = input("Enter your password: ")

    # Simulate basic authentication logic
    if user_password == "securepassword":
        print("Authentication successful!")
    else:
        print("Authentication failed. Incorrect password.")

if __name__ == "__main__":
    authenticate_user()

# main.py

def authenticate_user(username, password):
    # Critical fix: prevent empty username or password
    if not username or not password:
        return False

    if username == "admin" and password == "admin123":
        return True
    return False

def main():
    print("Application started")

if __name__ == "__main__":
    main()
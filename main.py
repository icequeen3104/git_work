def authenticate_user(username, password):
    # Hotfix: prevent empty username or password
    if not username or not password:
        return False

    # WIP refactor: use dictionary for credentials
    credentials = {
        "admin": "admin123",
        "user": "user123"
    }
    if username in credentials and credentials[username] == password:
        return True

    return False
"""
Account Manager - User registration and credentials onboarding.
"""

def register_user(first_name, last_name, email, age, country, role):
    full_name = first_name + " " + last_name
    return {"name": full_name, "email": email, "age": age, "country": country, "role": role}

def create_account():
    return register_user("John", "Doe", "john@example.com", 30, "USA", "developer")

if __name__ == "__main__":
    print("New profile:", create_account())

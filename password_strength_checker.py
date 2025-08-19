# password_strength_checker.py
print("running password strength checker...")
import re
import string
import random

def check_password_strength(password: str) -> str:
    """Check strength of a given password"""
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)
    
    if score == 5:
        return "Strong ✅"
    elif 3 <= score < 5:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

def generate_password(length=12) -> str:
    """Generate a strong random password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    while True:
        choice = input("\n1. Check Password Strength\n2. Generate Strong Password\n3. Exit\nChoose: ")
        
        if choice == "1":
            pwd = input("Enter password to check: ")
            print("Strength:", check_password_strength(pwd))
        elif choice == "2":
            print("Generated Password:", generate_password())
        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")
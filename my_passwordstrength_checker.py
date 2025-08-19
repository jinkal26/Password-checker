import time

# password_utils.py

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(ch.islower() for ch in password):
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch in "!@#$%^&*()_+-=[]{},.<>?/|" for ch in password):
        score += 1

    if score == 5:
        return "Strong ✅"
    elif score >= 3:
        return "Moderate ⚠️"
    else:
        return "Weak ❌"

def suggest_strong_password(length=12):
    if length < 8:
        length = 8
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    symbols = "!@#$%^&*()_+-=[]{},.<>?/|"
    chars = lowercase + uppercase + digits + symbols

    def pseudo_random(seed):
        a = 1664525
        c = 1013904223
        m = 2**32
        while True:
            seed = (a * seed + c) % m
            yield seed

    seed = int(time.time() * 1000)
    rng = pseudo_random(seed)

    while True:
        password = ''
        for _ in range(length):
            idx = next(rng) % len(chars)
            password += chars[idx]
        if check_password_strength(password) == "Strong ✅":
            return password

# Example usage:
if __name__ == "__main__":
    user_password = input("Enter a password to check its strength: ")
    print("Strength:", check_password_strength(user_password))
    print("Suggested strong password:", suggest_strong_password())
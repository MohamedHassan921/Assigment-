import itertools
import string

# Predefined dictionary of passwords
DICTIONARY = ["password", "123456", "admin", "letmein", "welcome", "monkey", "sunshine", "password1", "qwerty"]

def dictionary_attack(username):
    """
    Perform a dictionary attack using a predefined list of passwords.
    """
    print("Starting Dictionary Attack...")
    for password in DICTIONARY:
        print(f"Trying password: {password}")
        if login(username, password):
            print(f"Dictionary Attack Successful! Password for {username} is: {password}")
            return True
    print("Dictionary Attack Failed. No matching password found.")
    return False

def brute_force_attack(username):
    """
    Perform a brute-force attack to crack a 5-character alphabetical password.
    """
    print("Starting Brute Force Attack...")
    chars = string.ascii_letters  # A-Z, a-z
    password_length = 5
    attempts = 0

    # Try all possible combinations
    for guess in itertools.product(chars, repeat=password_length):
        attempts += 1
        guess = ''.join(guess)
        print(f"Attempt {attempts}: Trying password: {guess}")
        if login(username, guess):
            print(f"Brute Force Attack Successful! Password for {username} is: {guess}")
            return True
    print("Brute Force Attack Failed. No matching password found.")
    return False

def login(username, password):
    """
    Simulate a login attempt. Replace this with actual login logic if needed.
    """
    # Replace this with the actual password to crack
    correct_password = "hello"
    return password == correct_password

def main():
    # Prompt the user for a username
    username = input("Enter username: ")

    # First, try a dictionary attack
    if not dictionary_attack(username):
        # If dictionary attack fails, try a brute-force attack
        brute_force_attack(username)

if _name_ == "_main_":
    main()
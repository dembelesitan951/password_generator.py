import random
import string

def generate_password(length, complexity):
    chars = []
    if complexity == "easy":
        chars = string.ascii_letters
    elif complexity == "medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(chars)

    return password

password_length = int(input("Enter password length: "))
password_complexity = input("Enter password complexity (easy, medium, hard): ")

print("Password: ", generate_password(password_length, password_complexity))

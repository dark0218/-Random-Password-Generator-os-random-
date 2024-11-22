import os
import random
import string

def generate_password(length=12, use_special_chars=True, use_digits=True, use_uppercase=True, use_lowercase=True):
    if not (use_special_chars or use_digits or use_uppercase or use_lowercase):
        raise ValueError("At least one character type must be selected.")

    char_pools = []
    if use_special_chars:
        char_pools.append(string.punctuation)
    if use_digits:
        char_pools.append(string.digits)
    if use_uppercase:
        char_pools.append(string.ascii_uppercase)
    if use_lowercase:
        char_pools.append(string.ascii_lowercase)

    all_chars = ''.join(char_pools)
    password = ''.join(random.SystemRandom().choice(all_chars) for _ in range(length))

    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    password = generate_password(length)
    print(f"Generated Password: {password}")

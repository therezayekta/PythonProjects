import secrets
import string
import sys

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation
ALL_CHARACTERS = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

MIN_LENGTH = 8


def print_banner():
    print("=" * 40)
    print("        PASSWORD GENERATOR")
    print("=" * 40)


def generate_password(length):
    # Guarantee at least one of each character type
    password = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]
    for _ in range(length - 4):
        password.append(secrets.choice(ALL_CHARACTERS))

    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def check_strength(password):
    has_lower = any(c in LOWERCASE for c in password)
    has_upper = any(c in UPPERCASE for c in password)
    has_digit = any(c in DIGITS for c in password)
    has_symbol = any(c in SYMBOLS for c in password)
    score = sum([has_lower, has_upper, has_digit, has_symbol])

    if len(password) >= 16 and score == 4:
        return "Strong"
    elif len(password) >= 12 and score >= 3:
        return "Medium"
    else:
        return "Weak"


def main():
    print_banner()

    try:
        length = int(input(f"\n  Length (min {MIN_LENGTH}): ").strip())
    except ValueError:
        print("[!] Enter a valid number.")
        sys.exit(1)

    if length < MIN_LENGTH:
        print(f"[!] Minimum length is {MIN_LENGTH}.")
        sys.exit(1)

    password = generate_password(length)
    strength = check_strength(password)

    print(f"\n  Password  : {password}")
    print(f"  Length    : {len(password)}")
    print(f"  Strength  : {strength}")


if __name__ == "__main__":
    main()

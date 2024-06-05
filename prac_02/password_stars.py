def main():
    MIN_LENGTH = 8
    password = get_valid_password(MIN_LENGTH)
    print_asterisks(password)


def get_valid_password(min_length):
    password = input(f"Enter a password (minimum {min_length} characters): ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long. Please try again.")
        password = input(f"Enter a password (minimum {min_length} characters): ")
    return password


def print_asterisks(password):
    print('*' * len(password))


main()
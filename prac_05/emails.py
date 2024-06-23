def main():
    email_to_name = {}
    email = input("Emails: ")
    while email != "":
        name = get_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ")
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name(email):
    symobol = email.split("@")[0]
    dots = symobol.split(".")
    name = ".".join(dots).title()
    return name


main()

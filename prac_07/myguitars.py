from guitar import Guitar


def main():
    guitars = load_guitars()
    guitars.sort()
    display_guitars(guitars)
    add_guitars(guitars)


def load_guitars():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    in_file = open("guitars.csv", "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    return guitars


def add_guitars(guitars):
    """add guitars"""
    name = input("Name:")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
    with open("guitars.csv", 'w') as file:
        out_file = open("guitars.csv", "w")
        for guitar in guitars:
            out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
        out_file.close()


def display_guitars(guitars):
    """display the details of guitar"""
    for guitar in guitars:
        print(guitar)


main()
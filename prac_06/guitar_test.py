from prac_06.guitar import Guitar

Year = 2017


def test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    print(f"My guitar: {name}, first made in {year}")

    guitar = Guitar(name, year, cost)
    other = Guitar("Another Guitar", 2012, 1512.9)

    print(f"{guitar} get_age() - Expected {95}. Got {guitar.get_age()}")
    print(f"{other} get_age() - Expected {9}. Got {other.get_age()}")
    print(f"{guitar} is_vintage() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other} is_vintage() - Expected {False}. Got {other.is_vintage()}")


if __name__ == '__main__':
    test()
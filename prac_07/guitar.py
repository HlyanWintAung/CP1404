class Guitar:
    def __init__(self, name, year=0, cost=0):
        """Initialise guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """display the final string"""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """returns how old the guitar is in years"""
        current_year = 2022
        return current_year - self.year

    def is_vintage(self):
        """returns True if the guitar is 50 or more years old, False otherwise"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """sorting guitars by year"""
        return self.year < other.year
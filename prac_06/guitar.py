Year = 2017
vintage = 50


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self, name="", year=0, cost=0):
        return f"{self.name} ({self.year}) : $ {self.cost:,.2f}"

    def get_age(self):
        age = Year - self.year
        return age

    def is_vintage(self):
        return self.get_age() >= vintage

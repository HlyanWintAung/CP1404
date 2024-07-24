import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise project instance."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """return a string"""
        return f"{self.name}, start: {self.start_date}, priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """make the project is sorting by priority"""
        return self.priority < other.priority

    def is_completed(self):
        """if the project is complete, return the completion percentage to 100%"""
        return self.completion_percentage == 100



from car import Car
import random
class UnreliableCar(Car):
    """Represent a car that may or may not drive based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the car a given distance based on its reliability."""
        if random.random() * 100 < self.reliability:
            return super().drive(distance)
        else:
            return 0
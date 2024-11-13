"""File to define Fish class."""


class Fish:
    age: int

    def __init__(self):
        """create attributes."""
        self.age = 0
        return None

    def one_day(self):
        """Increase value of age attribute by 1."""
        self.age += 1
        return None

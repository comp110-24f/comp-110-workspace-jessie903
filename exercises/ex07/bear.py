"""File to define Bear class."""


class Bear:
    age: int
    hunger_score: int

    def __init__(self):
        """Create attributes."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Increase value of age attribute by 1."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """updates Bear's hunger score to increase by num_fish"""
        self.hunger_score += num_fish
        return None

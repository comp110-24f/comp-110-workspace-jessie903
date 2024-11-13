"""File to define River class."""

__author__ = "730473257"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Removing animals from River as they age."""
        # create lists to store fish who reach the age limit
        update_bears: list[Bear] = []
        update_fish: list[Fish] = []
        # iteratie through bears, adding to update_bears if less than 5
        for bear in self.bears:
            if bear.age <= 5:
                update_bears.append(bear)
        self.bears = update_bears
        # iterate through fish, adding to update_fish if less than 3
        for fish in self.fish:
            if fish.age <= 3:
                update_fish.append(fish)
        self.fish = update_fish
        return None

    def bears_eating(self):
        """Allow bears to eat if there are enough fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:  # Check for at least 5 in the river
                self.remove_fish(3)  # Bear will eat 3 fish
                bear.eat(3)  # Update bear's hunger by num_fish
            else:
                break
        return None

    def check_hunger(self):
        """Remove bears from the river if hunger score is less than 0."""
        # Create new list to hold bears with hunger score of 0 or higher
        survive_bears = []
        # Check if hunger_score is higher than 0, update new list if so
        for bear in self.bears:
            if bear.hunger_score >= 0:
                survive_bears.append(bear)
        self.bears = survive_bears
        return None

    def repopulate_fish(self):
        """Add new fish to the river based on num of existing fish."""
        # Calculate num of new fish to add
        new_fish = (len(self.fish) // 2) * 4
        # Add new fish to the river
        for _ in range(new_fish):
            # Create new fish, and add to the preexisting list
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Add new bears to the riber based on num of existing bears."""
        # Figure out num of new bears to add
        new_bears = len(self.bears) // 2
        # Add new bears to the river
        for _ in range(new_bears):
            self.bears.append(Bear())
        return None

    def view_river(self):
        """Tells you what day, and the number of fish and bear in the River."""
        fish_count = len(self.fish)
        bears_count = len(self.bears)
        print(f" ~~Day~~ {self.day}:")
        print(f"Fish Population: {fish_count} ")
        print(f"Bear Population: {bears_count} ")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Calls one_river_day 7 times."""
        for _ in range(7):
            self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Remove specified amount of fish from front of list."""
        while amount > 0 and len(self.fish) > 0:
            self.fish.pop(0)  # remove the fish at index 0
            amount -= 1  # Decrease the amount by 1 after removing fish

"""Plan for a Cozy Tea Party and Expenses"""

__author__: str = "730473257"


def main_planner(guests: int) -> None:
    """Main function that calls each other function and produces printed output"""
    tea_count: int = tea_bags(
        people=guests
    )  # How much tea will we need based on people, which is guests in this context
    treat_count: int = treats(
        people=guests
    )  # how many treats will we need based on the same thing as above
    total_cost: float = cost(tea_count=tea_count, treat_count=treat_count)
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_count))
    print("Treats: " + str(treat_count))
    print("Cost: $" + str(total_cost))
    return None


# defining tea bag function
def tea_bags(people: int) -> int:
    """Number of Tea Bags needed based on guest number"""
    return people * 2


# defining treats function
def treats(people: int) -> int:
    """Number of treats needed based on number of tea guests are expected to drink"""
    tea_count = tea_bags(
        people=people
    )  # use function wihtin function (peoploe*2 is already known)
    return int(
        tea_count * 1.5
    )  # returning total treats needed based on amount of tea drank


# defining cost function
def cost(tea_count: int, treat_count: int) -> float:
    """Function to compute the cost of the tea bags and the treats combined"""
    tea_price = 0.50  # individual tea price
    treat_price = 0.75  # individual treat price
    total_cost = (tea_count * tea_price) + (treat_count * treat_price)
    return total_cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))

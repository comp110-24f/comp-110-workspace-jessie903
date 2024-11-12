"""Pracitce with functions."""

from random import randint

print(randint(2, 54439))


# Function Definition!!!
def sum(num1: int, num2: int) -> int:
    """Return the sum of num1 and num2."""
    return num1 + num2


# Function Call
print(sum(num1=2, num2=13))


def fuel_needed(distance: int, mpg: int) -> float:
    return distance / mpg


def total_fuel_cost(distance: int, mpg: int, price_per_gallon: int) -> float:
    return fuel_needed(distance=distance, mpg=mpg) * price_per_gallon


print(total_fuel_cost(distance=300, mpg=25, price_per_gallon=4))

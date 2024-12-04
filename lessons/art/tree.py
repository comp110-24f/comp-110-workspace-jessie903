"""Some happy, little trees."""

from .turtle import Turtle
from math import pi

# from random import random

__template__ = "https://24ss2.comp110.com/static/turtle/"

DEGREE: float = -pi / 180.0  # Constant


def click(x: float, y: float) -> Turtle:
    """Moves trutles to wherevere we click on the canvas"""
    t: Turtle = Turtle()
    t.setSpeed(0.25)
    t.moveTo(x, y)
    t.turnTo(90 * DEGREE)

    # Declare length variable
    length: float = 150.0
    while length > 0.0:
        t.forward(length)
        t.left(pi / 2.0 - pi / 8.0)
        length -= 2.0
    branch(t, 100.0, 90 * DEGREE)

    return t


def branch(t: Turtle, length: float, angle: float) -> None:
    t.turnTo(angle)
    t.forward(length)
    # Magic Art happens here
    if length > 3.0:
        # Goal is to call branch function recursively
        branch(t, length * 0.75, angle + 35.0 * DEGREE)
        branch(t, length * 0.75, angle - 35.0 * DEGREE)
        # Use length 75%
    t.turnTo(angle + pi)
    t.forward(length)

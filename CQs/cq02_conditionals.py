"""Practice with Conditionals, Local Variables, and User Input"""

__author__ = "730473257"


def guess_a_number() -> None:
    secret: int = 7  # secret is the number the person is trying to guess
    guess: int = int(input("Guess a number:"))  # input a number; the person is guessing
    print("Your guess was " + str(guess))
    if guess == secret:  # "Then" if they guess the right number
        print("You got it!")
    elif guess < secret:  # If they guess a number lower than the secret number
        print("Your guess was too low! The secret number is " + str(secret))
    elif guess > secret:  # If they guess a number higher than the secret number
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()

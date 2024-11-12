"""Wordle game"""

__author__ = "730473257"


# CHECKS LENGTH OF INPUT FOR CORRECTNESS
def input_guess(secret_word_len: int) -> str:
    guess = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) == secret_word_len:  # returns the word if it is right # chars
        return guess
    while (
        len(guess) != secret_word_len
    ):  # keeps the loop going until right # chars is input
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess  # return the word after 2nd while loop is exited


# function that will test each index of the first parameter string to see if it matches the second parameter
def contains_char(secret_word: str, char_guess: str) -> bool:
    """Character parameter will assess word for instances of character wihtin word"""
    assert len(char_guess) == 1
    index = 0  # need to have this to allow the while loop in increase index and move through word
    while index < len(
        secret_word
    ):  # while indexing through word, return true if indices of char come up in word
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False  # if not indices of char within word, return false


# using emojis to tell accuracy of guess
def emojified(guess: str, secret: str) -> str:
    """USE INDEX TO GO THOROUGH GUESS AND DETERMINE IF THE INDEX CHAR == INDEX GUESS"""
    assert len(guess) == len(secret)  # make sure len of guess is same as secret word
    WHITE_BOX: str = "\U00002B1C"  # all 3 of these are storing the emoji code
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index = 0
    result = ""  # used to add the code for emojis in as index through word
    while index < len(guess):
        if guess[index] == secret[index]:
            result += GREEN_BOX  # if secret char is same index as guess char, add green box to str
        elif contains_char(secret, guess[index]):
            result += YELLOW_BOX  # guess char is in word, but not right spot = add yellow box to str
        else:
            result += WHITE_BOX  # guess not in secret, add white box to str
        index += 1  # increase index to go through guess
    return result  # gives the result of indexing through secret word chars to find matches of guess chars


# MAIN FUNCTION THAT CONTROLS GAME
def main(secret: str) -> None:  # secert word player is trying to guess
    """The entrypoint of program and main game loop."""
    assert len(secret) > 0  # make sure the secret word is not empty
    max_turns = 6
    turn_count = 0
    while turn_count < max_turns:  # limits player to 6 guesses
        turn_count += 1
        print(f" === Turn {turn_count}/{max_turns} === ")
        guess = input_guess(
            len(secret)
        )  # make sure guess is smae length as secret, if not input_guess is run
        results = emojified(
            guess, secret
        )  # use emoji function to label the different chars
        print(results)
        if guess == secret:  # when they guess the right word, all
            print(f"You won in {turn_count}/{max_turns}! ")
            return
    print(
        f"X/{max_turns} - Sorry, try again tomorrow! "
    )  # if they take more than 6 tries, prints this


if __name__ == "__main__":  # used to be able to call function, and be known as module
    main(secret="codes")

"""EX02 - Chardle -  A cute step toward Wordle."""

__author__ = "730473257"


def input_word() -> str:
    """Ask the user to input a 5-character word"""
    word: str = input("Enter a 5-character word: ")  # local variable stores their input
    if len(word) == 5:  # if word=5 characters, return word
        return word
    else:  # anyting else=print this
        print("Error: Word must contain 5 characters.")
        exit()  # exit the function if the input word is not 5 characters


def input_letter() -> str:
    """Asks person to input a single character"""
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter  # if letter is only one character return letter inputed
    else:
        print("Error: Character must be a single character")
        exit()  # makes letter not print if more than 1 character
        return letter  # return letter if more than 1 character


def contains_char(word: str, letter: str) -> None:
    """Indices when input character matches the characters within input word"""
    print(
        "Searching for " + letter + " in " + word
    )  # print this basically always from my understanding
    count: int = 0  # start at 0 matches for letters within word
    if word[0] == letter:
        print(letter + " found at index 0")
        count += (
            1  # when match is found, add one to the count variable (for each round 1-4)
        )
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1
    if count == 0:  # if no instances of letter in word, print following statment
        print("No instances of " + letter + " found in " + word)
    elif count == 1:  # if 1 instance of letter in word, print statement
        print("1 instance of " + letter + " found in " + word)
    else:  # if instances > 1, print the count that is calculated during the function
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:  # this functions calls all other functions; main function!
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()

"""Practice with Conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if num = 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number")
    else:
        print("Big number")
    print("Have a nice day")


less_than_10(num=5)


def should_i_eat(hungry: bool) -> bool:
    """Tells me whether or not to eat based on hunger"""
    if hungry:  # COndition/bool expression
        print("eat")  # "Then" block
    else:
        print("do your homework instead")  # "else" block
    print("I am proud of you!")  # either way, this is printed


should_i_eat(hungry=True)  # prints "eat" and "i am proud of you!"


def check_first_letter(word: str, letter: str) -> str:
    """Tells me if the first character of word is letter"""  # docstring
    if word[0] == letter:  # boolean expression
        return "match!"  # "Then" block
    else:
        return "no match!"  # "Else" block


print(check_first_letter(word="haopy", letter="h"))  # MATCH
print(check_first_letter(word="happy", letter="s"))  # NOMATCH


def get_weather_report() -> str:
    """Display weather instructions."""
    weather: str = input("What is the weather?")  # INPUT FUNCTION: DISPLAYS TO PERSON
    if weather == "rainy" or weather == "cold":
        print("Bring a jacket.")
    elif weather == "hot":
        print("Keep it cool out there")
    else:
        print("I don't recognize this weather.")
    return weather


get_weather_report()

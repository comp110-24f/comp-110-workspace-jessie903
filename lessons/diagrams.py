from random import randint


print("Hello" + " World")
print(randint(1, 3452))


def flavor(taste: str, percent: float) -> None:
    print("This flavor is " + str(percent) + "% " + taste)


flavor(taste="umami", percent="100.0")  # type: ignore


def name_eval(id: str) -> bool:
    print("Jessica" + "Avery")
    return name_eval  # type: ignore


def number_info(num: int) -> int:
    if num < 10:
        print("Small number.")
    else:
        if num % 2 == 0:
            print("EVen number.")
        else:
            print("Odd number.")
    return num


number_info(num=11)
print(number_info(num=4))


def characters(msg: str) -> None:
    index: int = 0
    while index < len(
        msg
    ):  # while index is less than the length of message, continue loop
        print(msg[index])  # print the letter of that index
        index = index + 1  # add one to index, and see if loop can be completed


characters(msg="Howdy")

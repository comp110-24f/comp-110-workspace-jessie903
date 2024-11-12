__author__ = "730473257"


def invert(input: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    for key, value in input.items():
        if value in inverted_dict:
            raise KeyError(f"Duplicate value found: {value}")
        inverted_dict[value] = key
    return inverted_dict


def favorite_color(favs: dict[str, str]) -> str:
    if len(favs) == 0:
        return ""
    color_count: dict[str, int] = {}
    for color in favs.values():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    most_pop_color = ""
    max_count = 0
    for color in color_count:
        if color_count[color] > max_count:
            most_pop_color = color
            max_count = color_count[color]
    return most_pop_color


def count(values: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in values:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    alphabetized_dict: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower()  # first letter of word in lowercase
        if (
            first_letter in alphabetized_dict
        ):  # check if first letter is already a key in dict
            alphabetized_dict[first_letter].append(word)  # append the word to list
        else:
            alphabetized_dict[first_letter] = [
                word
            ]  # initialize new list with the word
    return alphabetized_dict


def update_attendance(attendence: dict[str, list[str]], day: str, student: str) -> None:
    if day not in attendence:  # create new list for day if doesn't exist
        attendence[day] = []
    if student not in attendence[day]:  # add student to days list if they're not on it
        attendence[day].append(student)

""" Some scope examples """


def remove_chars(msg: str, char: str) -> str:
    """return a copy of msg with all instances of char removed"""
    copy: str = ""  # SET UP EMPTY STRING AND THEN WE CAN COPY VALUES OVER
    index: int = 0  # local variables
    while index < len(msg):
        if msg[index] != char:  # IF LETTER IS NOT CHAR
            copy += msg[index]  # ADD IT TO COPY (copy= copy + msg)
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # global variable
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))

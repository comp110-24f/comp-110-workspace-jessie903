__author__ = "730473257"


def mimic(message: str) -> str:
    """Repeat message back"""
    return message


# MAIN FUNCTION DEF
def main() -> None:
    """Print the result of calling mimic"""
    print(mimic(message=input("What is your message")))


if __name__ == "__main__":
    main()

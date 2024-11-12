def concat(msg1: str, msg2: str) -> str:
    """Returns the concatenation of the two input strings"""
    return msg1 + msg2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))

x: str = "123"
y: str = "abc"
print(concat(x, y))

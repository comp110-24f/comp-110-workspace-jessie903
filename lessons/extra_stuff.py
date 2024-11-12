def chars(msg: str) -> str:
    idx: int = 0
    copy: str = msg
    while idx < len(msg):
        print(msg[idx])
        idx += 1
    return copy


a: str = "Hey"
b: str = "Hi"
chars(msg=a)


def double(x: int) -> int:
    return x * 2


def double_display(y: int) -> int:  # type: ignore
    print(y * 2)


double_display(2)

if __name__ == "__main__":
    print(double(3))

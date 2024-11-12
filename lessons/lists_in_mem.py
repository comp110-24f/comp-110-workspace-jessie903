"""Lists in Memory"""

x: list[float] = [1.0, 2.0]
y: list[float] = [3.0, 4.0]
y = x
x[0] = 3.0
print(x)
print(y)


def view(my_list: list[str]):
    idx: int = 0
    while idx < len(my_list):
        print(my_list[idx])
        idx += 1


msg: list[str] = ["Hello", "World"]
print(view(msg))

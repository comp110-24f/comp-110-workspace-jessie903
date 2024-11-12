def get_coords(xs: str, ys: str) -> None:
    """Prints the formatted pairs of each character in the two input strings"""
    a: int = 0  # index variable for xs
    while a < len(xs):  # outer loop that iterates for xs
        b: int = 0  # index variable for ys
        while b < len(ys):  # inner loop that iterates over ys
            print("(" + xs[a] + "," + ys[b] + ")")  # print pairs of letters
            b += 1  # add to index, move to next character in ys
        a += 1  # add, move to next character in xs

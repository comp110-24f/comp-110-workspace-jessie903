"""An example of recursive functions"""


def factorial(n: int) -> int:
    """Complete the factorial of n."""
    # Base case
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

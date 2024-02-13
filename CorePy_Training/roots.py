"""_summary_
"""
import sys


def sqrt(x):
    """_summary_

    Args:
        x (integer): The number of which the square root is to be computed.

    Returns:
        guess: The square root of x.

    Raises:
        ValueError: If x is negative.
    """
    if x < 0:
        raise ValueError(
            "Cannot compute square root of "
            f"negative numbers: '{x}'"
            )

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    """_summary_"""
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:         # 'e' is the captured error message
        print(e, file=sys.stderr)
    print("=== program continue ====")


if __name__ == "__main__":
    main()

# end of main

"""
Summary:
    Calculate the logaithm of a number given its string representation from a dictionary of number.

Usage:
    python convert("string_number".split())
    python string_log("string_numbers".split())
"""

import sys
from math import log


DIGIT_MAP = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def convert(s):
    """Convert a string to an integer.

    Args:
        s (string): the input number(s) in the dictionnary, as string

    Returns:
        x: the resulting number in the dictionary of integers; -1 being the error indicator
    """
    try:
        number = ""                         # string number
        for token in s:                     # iterates over each token (word) in the input list s.
            number += DIGIT_MAP[            # appends the corresponding numerical digit from the DIGIT_MAP dictionary to the number string
                token
            ]
        return int(number)                  # converts the resulting number string to an integer x
                                            # print(f"Conversion succeded! x = {x}")
    except (
        KeyError,
        TypeError,
    ) as e:                                 # e is used to catch the error message; !r give indepth details on the error
        print(
            f"Conversion error: {e!r}",     # PRINT statement is used for debugging, use PASS when issue resolved
            file=sys.stderr,                # system standard error
        ) 
        raise                               # RAISE the exception details is better than RETURNning the error code -1


def string_log(s):
    """
    Calculate the logarithm of a number represented as a string.

    Args:
        s (str): The input number(s) in the dictionary, as a string.

    Returns:
        v (float): The logarithm of the converted number.
    """
    v = convert(s)
    return log(v)

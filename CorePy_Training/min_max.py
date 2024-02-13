"""
Summary:
    Find the minimum and maximum values in a list of integers.

Usage:
    min_max([list of integers])
"""


def min_max(items):
    """
    Find the minimum and maximum values in a list of integers.

    Args:
        items (list): A list of integers.

    Returns:
        tuple: A tuple containing the minimum and maximum values.
    """
    return min(items), max(items)

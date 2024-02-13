############################################ combination of filter() and reduce()
from functools import reduce

def combine_reduce_filter(func, iterable):
    """
    This function combines the use of 'filter()' and 'reduce()' on an iterable.
    It first applies 'filter()' to the iterable with 'func' as the predicate, then applies 'reduce()' to the result to combine the remaining elements.
    'func' should be a function that takes one argument and returns a boolean.
    'iterable' should be an iterable of elements that can be combined with the '+' operator.
    """

    # Apply 'filter()' to the iterable with 'func' as the predicate.
    # This removes elements for which 'func' returns False.
    filtered_iterable = filter(func, iterable)

    # Apply 'reduce()' to the result of 'filter()'.
    # This combines the remaining elements with the '+' operator.
    result = reduce(lambda x, y: x + y, filtered_iterable)

    # Return the result
    return result

# Define a list of numbers
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# Define a function that returns True for positive numbers and False for non-positive numbers
is_positive = lambda x: x > 0

# Use 'combine_reduce_filter()' to add together only the positive numbers in the list
# This first removes the non-positive numbers from the list with 'filter()', then adds together the remaining numbers with 'reduce()'
sum_of_positive_numbers = combine_reduce_filter(is_positive, numbers)  # 25

# Print the result
print(sum_of_positive_numbers)  # 25


############################################ combination of map() and filter()
# Define a list of numbers
numbers = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

# Use 'filter()' to remove non-positive numbers, then 'map()' to square the remaining numbers
squared_positive_numbers = map(lambda x: x**2, filter(lambda x: x > 0, numbers))

# Convert the result to a list to see the elements
print(list(squared_positive_numbers))  # [1, 9, 25, 49, 81]


############################################ combination of map() and reduce()
from functools import reduce

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Use 'map()' to square the numbers, then 'reduce()' to add the squares together
sum_of_squares = reduce(lambda x, y: x + y, map(lambda x: x**2, numbers))

# Print the result
print(sum_of_squares)  # 55
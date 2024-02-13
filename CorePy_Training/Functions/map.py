""" use case of map() with multiple iterables"""

# Define three lists of strings
sizes = ['small', 'medium', 'large']
colors = ['lavender', 'orange', 'green']
animals = ['koala', 'lion', 'elephant']


# Define a function that takes three arguments and returns a string that combines them
def combine(size, color, animal):
    """
    This function takes three arguments and returns a string that combines them.
    It's used as the function argument to 'map()'.
    """
    return f'{size} {color} {animal}'


# The 'map()' function applies the 'combine' function to each group of elements at the same index in 'sizes', 'colors', and 'animals'.
# It returns an iterable, which is then converted to a list.
# The result is a list of strings where each string is a combination of a size, a color, and an animal.
list_combination = list(map(combine, sizes, colors, animals))  # ['small lavender koala', 'medium orange lion', 'large green elephant']

# Print the list of combinations
print(list_combination)

###################################################### map() vs comprehension
# performance: neither map() nor map() is faster than the other
# Readability: map() is less readable than list comprehension
# Context: the choice between map() and list comprehension depends on the context

###################################################### example with list comprehension
# Define three lists of strings
sizes = ['small', 'medium', 'large']
colors = ['lavender', 'orange', 'green']
animals = ['koala', 'lion', 'elephant']

# Use list comprehension to create a new list where each element is a combination of a size, a color, and an animal.
# This is equivalent to using 'map()' with the 'combine' function.
list_combination = [f'{size} {color} {animal}' for size, color, animal in zip(sizes, colors, animals)]  # ['small lavender koala', 'medium orange lion', 'large green elephant']

# Print the list of combinations
print(list_combination)
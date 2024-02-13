""" filter(function, sequence) 
    - The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
    - The filter() function returns an iterator, so you need to convert it to a list to see the elements.
    - The function must return a boolean value (True or False).
    - The sequence can be any iterable, like a list, tuple, set, etc.
    - The filter() function does not modify the original sequence.
    - The filter() function can be used with a lambda function.
    - The filter() function is less readable than list comprehension.
    - The choice between filter() and list comprehension depends on the context.
"""

# here we apply lambda as filter() function to a list of numbers to return only the positive numbers
positives = filter(lambda x: x > 0, [1, -5, 0, 6, -2, 8])
print(positives)  # <filter object at 0x7f3f3c1e3a90>
print(list(positives))  # [1, 6, 8]

########## filter function where None is passed as the first argument to eliminates inputs which evaluate to false ####

# Define a list with some elements that evaluate to False
values = [0, "hello", None, -2, [], "world", "", 15, False]

# Use the 'filter()' function with 'None' as the first argument to eliminate elements that evaluate to False
# The 'filter()' function returns an iterator, so convert it to a list to see the elements
filtered_values = list(filter(None, values))  # ['hello', -2, 'world', 15]

# Print the filtered list
print(filtered_values)

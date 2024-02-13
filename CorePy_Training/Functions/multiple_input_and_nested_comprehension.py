"""
    notes:
        - comprehension can have multiple if-clauses,
        - comprehension can have multiple for-clauses,
        - comprehension can have be nested, and nested for loops can be used to create nested comprehension
        - multiple input and nested comprehension can be used to create a 'list', 'dictionary', 'set' or 'generator'.

"""

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a list of letters
letters = ['a', 'b', 'c', 'd', 'e']

# Use multiple-input comprehension to create a list of tuples
result = [(num, letter) for num in numbers for letter in letters]

# Print the result
#print(result)

#######

# comprhension format 1
values = [x / (x - y) for x in range (100) if x > 50 for y in range(100) if x - y != 0]

# comprhension format 2
values2 = [x / (x - y) 
          for x in range (100) 
          if x > 50 for y in range(100) 
          if x - y != 0]

#print(values)

""" 
non-comprhension format of values

values = []
for x in range (100) 
    if x > 50 
        for y in range(100) 
            if x - y != 0]
                values.append(x / (x - y))
"""


############### nested comprehensions functions
vals = [[y * 3 for y in range(x)] for x in range(10)]
""" 
outer = []
for x in range(10):
    inner = []
    for y in range(x):
        inner.append(y * 3)
    outer.append(inner)
"""

print(vals)

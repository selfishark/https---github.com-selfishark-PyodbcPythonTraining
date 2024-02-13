# Generator functions are identified by 'yield' statements and my include a return statement
    # they produce a sequence of values on-the-fly and maintain their state between calls.

# you can use the next() function to retrieve the next value from the generator

def generator123():
    """
    Summary:
    A generator function that yields the integers 1, 2, and 3.

    Usage:
    Call the generator123 function to obtain a generator object.
    Use the next() function to retrieve the next value from the generator.

    Example:
    ```
    gen = generator123()
    print(next(gen))  # Output: 1
    print(next(gen))  # Output: 2
    print(next(gen))  # Output: 3
    ```
    """
    print("About to yield 1")
    yield 1  # Yield the value 1 when the generator is iterated over
    print("About to yield 2")
    yield 2  # Yield the value 2 when the generator is iterated over
    print("About to yield 3")
    yield 3  # Yield the value 3 when the generator is iterated over
    print("About to yield 4")
    yield 4  # Yield the value 3 when the generator is iterated over
    print("About to yield 5")
    yield 5  # Yield the value 3 when the generator is iterated over
    print("About to return")

#usage 1
gen = generator123()

print(next(gen))
print(next(gen))
print(next(gen))

#usage 2
for i in generator123():
    print(i)  


#usage 3
# Generators allows to model infinite sequences for : large content files, mathematical sequences, sensor readings, etc.

def take(count, iterate):
    counter = 0
    for i in iterate:
        if counter == count:
            return      # this terminates the iteration
        counter += 1
        yield i         # yield the value


def distinct(iterate):
    seen = set()        # unique values already seen
    for i in iterate:
        if i in seen:
            continue    # this allow the iteration to roll over
        yield i         # yield the value
        seen.add(i)     # add only previously unseen value in the set


def run_pipeline():
    items = [3, 4, 4, 9, 5, 5, 8]       # define your list of items
    for i in take(3, list(distinct(items))):  # iterate over the items, select the first 3 and filter duplicates / list allows all items to be listed to facilitate the work of the take() method
        print(i)


run_pipeline()
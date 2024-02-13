####################################### function decorator ########################################

""" 
    Description:
        This code defines a decorator escape_unicode that can be used to modify the behavior of other functions. 
        It does this by defining a nested function wrap that calls the original function and then applies some additional behavior (in this case, converting the result to ASCII). 
        The decorator function then returns this wrapper function. When you apply this decorator to a function using the @escape_unicode syntax, it replaces the original function with the wrapper function. 
        This means that when you call the decorated function, you're actually calling the wrapper function, which in turn calls the original function and then applies the additional behavior.
        
        Decorators are functions that take another function as an argument and extend its behavior and functionality without modifying it. 
        Decorators are used to modify the behavior of a function or class.
        Decorators are a type of function that take a function as an argument and return a closure.
        Decorators wrap a function, modifying its behavior.
        Decorators are used to extend the functionality of a function or class.
        
    
    Usage example:
        @escape_unicode # decorator
        def northen_city():
            return 'Tromsø'
        print(northen_city()) # 'Troms\xf8'
"""


# Define a decorator function 'escape_unicode'
from mimetypes import suffix_map
from typing import Any


def escape_unicode(f):
    """
    This decorator function takes another function 'f' as an argument.
    It returns a new function 'wrap' that calls 'f' and then converts its result to ASCII.
    This is useful for ensuring that the output of f is always in ASCII, regardless of what string it returns.
    """

    # Define a wrapper function that takes any number of positional and keyword arguments
    def wrap(*args, **kwargs):
        # Call the function 'f' with the given arguments and capture its result in 'x'
        x = f(*args, **kwargs)
        # Convert 'x' to ASCII and return the result
        return ascii(x)

    # Return the wrapper function
    return wrap

# function without the decorator
def northen_city():
    """Returns a city in Norway"""
    return 'Tromsø'


print(northen_city())

# The '@escape_unicode' line is a decorator that modifies the behavior of the 'northen_city' function.
# When 'northen_city' is called, it's actually the 'wrap' function inside 'escape_unicode' that gets called.
# 'wrap' then calls 'northen_city', converts its result to ASCII, and returns the result.
@escape_unicode     # decorator
def northen_city():
    """Returns a city in Norway"""
    return 'Tromsø'


print(northen_city()) # 'Troms\xf8'

####################################### Classes decorator ########################################


class CallCount:
    """
    This class decorator keeps track of the number of times a function is called.
    This class is used as a decorator, which means it modifies the behavior of the function it decorates.
    """

    def __init__(self, f):
        """
        The constructor stores a reference to the function being decorated and initializes a count to zero.
        :param f: The function to be decorated.
        """
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwds):
        """
        This method is called when the decorated function is called.
        It increments the count and then calls the original function with the same arguments.
        :param args: Positional arguments to be passed to the function.
        :param kwds: Keyword arguments to be passed to the function.
        :return: The result of calling the decorated function.
        """
        self.count += 1
        return self.f(*args, **kwds)

# The '@CallCount' line is a decorator that modifies the behavior of the 'hello' function.
# When 'hello' is called, it's actually the '__call__' method of the 'CallCount' instance that gets called.
# '__call__' then increments the count, calls 'hello', and returns its result.
# This decorator example keeps track of how many times 'hello' has been called.
@CallCount
def hello(name):
    """
    Returns a greeting using the corresponding variable.
    :param name: The name to be included in the greeting.
    """
    print(f"Hello, {name}")


greeting1 = hello("Ludo")
print(hello.count)
greeting1 = hello("selfishark")
greeting1 = hello("Corporateshark")
print(hello.count)

######################################## Instances decorator ########################################


class Trace:
    """
    A class that represents a decorator as an instance. This decorator keeps track of how many times a function is called.
    Unlike a class decorator that directly decorates a function, an instance decorator uses an instance of a class to decorate the function.
    """

    def __init__(self):
        """
        The constructor initializes an 'enabled' attribute to True.
        This attribute can be used to turn the tracing behavior on and off.
        """
        self.enabled = True

    def __call__(self, f):
        """
        This method is called when the decorated function is called.
        It returns a wrapper function that calls the original function and prints a message if tracing is enabled.
        :param f: The function to be decorated.
        :return: The wrapper function.
        """

        def wrap(*args, **kwargs):
            """
            This is the wrapper function that gets called when the decorated function is called.
            If tracing is enabled, it prints a message and then calls the original function with the same arguments.
            :param args: Positional arguments to be passed to the function.
            :param kwargs: Keyword arguments to be passed to the function.
            :return: The result of calling the decorated function.
            """
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)
        return wrap


# Create an instance of the Trace class.
# This instance can be used as a decorator to trace calls to a function.
tracer = Trace()

# The '@tracer' line is a decorator that modifies the behavior of the 'rotate_list' function.
# When 'rotate_list' is called, it's actually the '__call__' method of the 'tracer' instance that gets called.
# '__call__' then calls 'rotate_list', and if tracing is enabled, prints a message.
@tracer
def rotate_list(l):
    """
    Rotates a list by moving the first element to the end of the list.
    :param l: The list to be rotated.
    """
    rotated_list = l[1:] + [l[0]]
    print("rotated_list", rotated_list)


list_in_order = [1, 2, 3]
rotate_list(list_in_order)


######################################## Multiple decorators ########################################

# Define a decorator function 'escape_unicode'
from typing import Any

def escape_unicode(f):
    """
    This decorator function takes another function 'f' as an argument.
    It returns a new function 'wrap' that calls 'f' and then converts its result to ASCII.
    This is useful for ensuring that the output of f is always in ASCII, regardless of what string it returns.
    """

    # Define a wrapper function that takes any number of positional and keyword arguments
    def wrap(*args, **kwargs):
        # Call the function 'f' with the given arguments and capture its result in 'x'
        x = f(*args, **kwargs)
        # Convert 'x' to ASCII and return the result
        return ascii(x)

    # Return the wrapper function
    return wrap


class Trace:
    """
    A class that represents a decorator as an instance. This decorator keeps track of how many times a function is called.
    Unlike a class decorator that directly decorates a function, an instance decorator uses an instance of a class to decorate the function.
    """

    def __init__(self):
        """
        The constructor initializes an 'enabled' attribute to True.
        This attribute can be used to turn the tracing behavior on and off.
        """
        self.enabled = True

    def __call__(self, f):
        """
        This method is called when the decorated function is called.
        It returns a wrapper function that calls the original function and prints a message if tracing is enabled.
        :param f: The function to be decorated.
        :return: The wrapper function.
        """

        def wrap(*args, **kwargs):
            """
            This is the wrapper function that gets called when the decorated function is called.
            If tracing is enabled, it prints a message and then calls the original function with the same arguments.
            :param args: Positional arguments to be passed to the function.
            :param kwargs: Keyword arguments to be passed to the function.
            :return: The result of calling the decorated function.
            """
            if self.enabled:
                print(f"Calling {f}")
            return f(*args, **kwargs)
        return wrap


# Create an instance of the Trace class.
# This instance can be used as a decorator to trace calls to a function.
tracer = Trace()

# The '@tracer' and '@escape_unicode' lines are decorators that modify the behavior of the 'norwegian_island_maker' function.
# When 'norwegian_island_maker' is called, it's actually the '__call__' method of the 'tracer' instance that gets called first.
# '__call__' then calls the 'wrap' function of 'escape_unicode', which in turn calls 'norwegian_island_maker'.
# This demonstrates the use of multiple decorators, where the decorators are applied from bottom to top.
@tracer
@escape_unicode
def norwegian_island_maker(name):
    """
    Returns a Norwegian island name.
    :param name: The name to be included in the island name.
    :return: The island name.
    """
    return name + 'øy'

norwegian_island_maker("lLaman")
norwegian_island_maker("python")
tracer.enabled = False
norwegian_island_maker("ai_city")
tracer.enabled = True
norwegian_island_maker("susser")



######################################## combine a decorator with a method ########################################

class IslandMaker:
    """
    A class that has a method which uses a decorator.
    The decorator is applied to the 'make_island' method, which means that when 'make_island' is called,
    it's actually the '__call__' method of the 'tracer' instance that gets called.
    """

    def __init__(self, suffix):
        """
        The constructor stores a suffix that will be added to the name to make an island name.
        :param suffix: The suffix to be added to the name.
        """
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        """
        Returns an island name by adding a suffix to the given name.
        Because of the '@tracer' decorator, when this method is called, it's actually the '__call__' method of the 'tracer' instance that gets called.
        '__call__' then calls this method and, if tracing is enabled, prints a message.
        :param name: The name to which the suffix will be added.
        :return: The island name.
        """
        return name + self.suffix


# Create an instance of the IslandMaker class with ' Island' as the suffix.
im = IslandMaker(' Island')

# Call the 'make_island' method of the 'im' instance.
# Because of the '@tracer' decorator, this actually calls the '__call__' method of the 'tracer' instance.
# '__call__' then calls the 'make_island' method and, if tracing is enabled, prints a message.
im.make_island('Samaries')

######################################## preserving a function metadata when wrapped by decorators ########################################

import functools

def noop(f):
    """
    This decorator function takes another function 'f' as an argument.
    It returns a new function 'noop_wrapper' that calls 'f'.
    The '@functools.wraps(f)' decorator is used to preserve the metadata of 'f'.
    """

    @functools.wraps(f)     # copy the function metadata (essential feature)
    def noop_wrapper():
        """
        This is the wrapper function that gets called when the decorated function is called.
        It simply calls the original function 'f'.
        """
        return f()

    # Return the wrapper function
    return noop_wrapper

@noop
def hello_world():
    """
    Prints 'Hello, world!'
    Because of the '@noop' decorator, when this function is called, it's actually the 'noop_wrapper' function that gets called.
    'noop_wrapper' then calls this function.
    The '@functools.wraps(f)' decorator in 'noop' ensures that the metadata of this function is preserved.
    """
    print("Hello, world!")


# Print the metadata of the 'hello_world' function.
help(hello_world)

# metadate to preserve : __name__ and __doc__

####################################### Parameterised decorator ########################################
import functools

def check_non_negative(index):
    """
    This is a parameterized decorator factory. It takes an index and returns a decorator.
    The returned decorator will validate that the argument at the given index of the decorated function is non-negative.
    """

    def validator(f):
        """
        This is the actual decorator function. It takes a function 'f' and returns a new function 'wrap'.
        The '@functools.wraps(f)' decorator is used to preserve the metadata of 'f'.
        """

        @functools.wraps(f)  # Apply the decorator here to preserve the metadata of 'f'
        def wrap(*args):
            """
            This is the wrapper function that gets called when the decorated function is called.
            It checks that the argument at the given index is non-negative, and if it is, it calls the original function 'f'.
            """
            if args[index] < 0:
                raise ValueError(f"Argument {index} must be non-negative")
            return f(*args)

        # Return the wrapper function
        return wrap

    # Return the decorator
    return validator


# The '@check_non_negative(1)' line is a parameterized decorator that checks that the second argument of 'create_list' is non-negative.
# When 'create_list' is called, it's actually the 'wrap' function inside 'validator' that gets called.
# 'wrap' then checks that the second argument is non-negative, and if it is, it calls 'create_list'.
@check_non_negative(1)
def create_list(value, size):
    """
    Returns a list of the given size where all elements are the given value.
    """
    return [value] * size


# Call 'create_list' with arguments 'a' and 3.
# This actually calls the 'wrap' function inside 'validator', which checks that the second argument is non-negative and then calls 'create_list'.
create_list('a', 3)
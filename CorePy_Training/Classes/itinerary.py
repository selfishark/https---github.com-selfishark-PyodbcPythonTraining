import functools
import inspect

class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= 90):
            raise ValueError(f"Latitude {latitude} is out of range; must be between -90 and 90.")

        if not (-180 <= longitude <= 180):
            raise ValueError(f"Longitude {longitude} is out of range; must be between -180 and 180.")

        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    def __repr__(self):
        # This method returns a string representation of an object
        # This is good practice, useful for the developer to see the object's state
        # The object's state represents attributes that are relevant to the object's identity
        # __repr__ is also useful for format the code output/result to be legitimate python source code, like a constructor call
        return f"{typename(self)}(latitude={self.latitude}, longitude={self.longitude})" # self represent the object type passed to typename() at runtime

    def __str__(self):
        # Just like __repr__ this method returns a string representation of an object; besides __repr__ inherits from __str__
        # This is good practice, intended for the end user for external representation
        # __str__() is the constructor used to display an object when using the print function / i.e: print("Cameroon geo coordinates are: ", Cameroon)
        # return (f"{abs(self.latitude)}° {self.latitude_hemisphere}, "
        #         f"{abs(self.longitude)}° {self.longitude_hemisphere}")
        # The default format invocation where format_spec is the empty string should give the same result as __str__
        return format(self)

    def __format__(self, format_spec: str) -> str:
        # format_spec must be used to match the signature of the method it's overriding
        # format_spec is used to specify the representation of a object such as floating point numbers, string, datetime to match a specific format specification
        # f-string and the format() of the str class delegates to the built-in format function which then delegates to __format__
        # this representation then impact f-string and format() method
        component_format_spec = ".2f"   # converts to two decimal places using a format specifier, .2f
        prefix, dot, suffix = format_specifier.partition(".")  # partition the format_specifier into prefix, dot, and suffix
        if dot:
            num_decimal_places = int(suffix)  # convert the suffix to an integer
            component_format_spec = f".{num_decimal_places}f"  # convert the suffix to a format specifier, .{num_decimal_places}f

        latitude = format(abs(self.latitude), component_format_spec)   # convert latitude to the assigned a format specifier, component_format_spec
        longitude = format(abs(self.longitude), component_format_spec)  # convert latitude to the assigned a format specifier, component_format_spec
        return (f"{latitude}° {self.latitude_hemisphere}, "
                f"{longitude}° {self.longitude_hemisphere}")


class EarthPosition(Position):
    pass


def typename(obj):
    # type(obj).__name__ is used to dynamically retrieve the name of the current object (at runtime) to avoid confusion in case of inheritance
    return type(obj).__name__

def auto_repr(cls):     # cls is used to avoid name clash with the 'class' keyword; which also represents the class to be decorated
    # print(f"Decorating {cls.__name__} with auto_repr")
    members = vars(cls)  # vars (a built-in function) is a mapping dictionary object that contains all the members of the class
    # for name, member in members.items():
        # print(f"{name}, {member}")

    if "__repr__" in members:
        raise TypeError(f"{cls.__name__} __repr__ already defined")

    if "__init__" not in members:
        raise TypeError(f"{cls.__name__} does not override __init__")

    # 'sig' will help to know that for every argument of __init__ beyond self there exist a property with the same name
    sig = inspect.signature(cls.__init__)  # inspect allows to inspect the signature of a function; and the signature of a function is the list of parameters it takes
    # Extract the list of parameter names in __init__ excluding the first parameter (self)
    parameter_names = [param.name for param in sig.parameters.values()][1:]

    # print(f"parameter_names: {parameter_names}")
    # print("__init__ parameters: ", sig.parameters)

    if not all(     # all (built-in property allows to below check to be done in all the parameter names)
        # check if the parameter name is of type property, otherwise is 'None'
        # the statement returns True if the object associated with name is a property, rather than irregular method
        isinstance(members.get(name, None), property)
        for name in parameter_names
    ):
        raise TypeError(f"Cannot apply auto_repr to {cls.__name__} because __init__ parameters must be properties")

    # The synthetised_repr method is created dynamically to support the __repr__ method when creating the class
    def synthetised_repr(self):
        return "{typename}({args})".format(
            typename=typename(self),
            args=", ".join(
                "{name}={value!r}".format(name=name, value=getattr(self, name))
                for name in parameter_names
            )
        )

    setattr(cls, "__repr__", synthetised_repr)  # setattr is a built-in function that allows to set an attribute of an object

    return cls


@auto_repr
class Location:
    """ The location class represents a geographical location on Earth.
        It helps automatically generate the __repr__ method for the class.
    """
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    def __str__(self):
        return self.name


def __repr__(self):
    return f"{typename(self)}(name={self.name}, position={self.position})"


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

# The postcondition function is a decorator factory. It takes a predicate function as an argument
# and returns a decorator (function_decorator) that can be used to wrap other functions.
def postcondition(predicate):
    # The returned decorator takes a function 'f' as an argument.
    def function_decorator(f):
        # It then creates a new function (wrapper) that wraps 'f'.
        @functools.wraps(f)
        def wrapper(self, *args, **kwargs):
            # This wrapper function first calls 'f' and stores its result.
            result = f(self, *args, **kwargs)
            # Then it calls the predicate function with 'self' as an argument.
            # If the predicate returns False, it raises a RuntimeError.
            if not predicate(self):
                raise RuntimeError(
                    f"Post-condition {predicate.__name__} not maintained for {self!r}."
                )
            # If the predicate returns True, it simply returns the result of 'f'.
            return result
        # The decorator returns the wrapper function.
        return wrapper
    # The decorator factory returns the decorator.
    return function_decorator

def no_duplicates(itinerary):
    # The decorator factory returns a decorator that can be used to wrap the Itinerary class.
    # It helps to ensure that an itinerary does not contain duplicate locations.
    already_seen = set()
    for location in itinerary._locations:
        if location in already_seen:
            return False
        already_seen.add(location)
    return True

def invariant(predicate):
    # The invariant function is also a decorator factory, similar to postcondition.
    # It takes a predicate function as an argument and returns a decorator (class_decorator) that can be used to wrap classes.
    # The returned decorator takes a class 'cls' as an argument.
    function_decorator = postcondition(predicate)  # Here, it uses the postcondition function to create a function decorator.
    def class_decorator(cls):
        # The class_decorator function takes a class 'cls' as an argument.
        members = list(vars(cls).items())
        for name, member in members:
            # It then iterates over the members of the class and checks if they are methods.
            if inspect.isfunction(member):
                # If a member is a method, it wraps the method with the function decorator created by postcondition.
                setattr(cls, name, function_decorator(member))
        # The class_decorator returns the class with the wrapped methods.
        return cls
    return class_decorator


# The at_least_two_locations function is a predicate function that can be used with the postcondition decorator.
# It takes an Itinerary object as an argument and returns True if the itinerary has at least two locations, and False otherwise.
def at_least_two_locations(itinerary):
    return len(itinerary._locations) >= 2


@auto_repr
@invariant(no_duplicates)
@invariant(at_least_two_locations)
class Itinerary:
    """ This class represents an itinerary, which is a list of locations on a journey.
        It provides methods to add and remove locations, and to truncate the itinerary at a specific location.
        The itinerary must always have at least two locations. This is enforced by the @invariant decorator,
        which uses the at_least_two_locations function as a predicate.

        The @invariant decorator is defined using the postcondition function, which in turn uses the @functools.wraps decorator.
        @functools.wraps is a built-in Python decorator for updating the __name__, __doc__, and other special attributes of the wrapper function
        it decorates with those of the original function. This is useful for debugging, as it ensures that the function's metadata remains intact.

        The @invariant decorator also uses the vars() function to get a dictionary of the class's attributes, and the setattr() function to set
        the value of each attribute. This allows it to wrap each method of the class with a function decorator that checks the postcondition
        after the method is called. If the postcondition is not met, the decorator raises an exception.
    """
    @classmethod
    # list constructor of locations arg's tuple forwarded to the initialiser
    def from_locations(cls, *locations):
        return cls(locations)

    # The postcondition decorator is used to specify a condition that must be true after the method has finished executing.
    # In this case, the condition is that there must be at least two locations.
    # If the condition is not met, the decorator will raise an exception.
    # @postcondition(at_least_two_locations) can be removed as @invariant(at_least_two_locations) already covers it 
    def __init__(self, locations):
        # Initialise the class with an iterable list of locations
        self._locations = list(locations)

    def __str__(self):
        # prints out a list of locations one per line
        return "\n".join(location.name for location in self._locations)

    @property
    def locations(self):
        # returns a sequence of locations with the locations
        return tuple(self._locations)

    @property
    def origin(self):
        # the beginning of the itinerary
        return self._locations[0]

    @property
    def destination(self):
        # the end of the itinerary
        return self._locations[-1]

    # Similar to __init__, the add method also has a postcondition that there must be at least two locations after the method has finished executing.
    # @postcondition(at_least_two_locations) can be removed as @invariant(at_least_two_locations) already covers it 
    def add(self, location):
        # add a new location to the list of locations of the itinerary
        self._locations.append(location)

    # The remove method also has a postcondition that there must be at least two locations after the method has finished executing.
    # @postcondition(at_least_two_locations) can be removed as @invariant(at_least_two_locations) already covers it 
    def remove(self, name):
        # remove a location in the journey by name

        # First, we create a list of indexes for all locations whose name matches the given name.
        # We use the enumerate function here, which returns pairs of (index, element) for each element in the list.
        removal_indexes = [
            index for index, location in enumerate(self._locations)
            if location.name == name
        ]

        # Then, we iterate over the list of indexes in reverse order.
        # We need to do this in reverse order to avoid issues with changing indexes after deletion.
        # For example, if we delete the element at index 0 first, all other elements will move one place to the left,
        # and their indexes will decrease by 1. So, if we then try to delete the element that was originally at index 1,
        # we would actually be deleting the element that is now at index 1, which is not what we want.
        # By deleting the elements from the end of the list first, we ensure that we're deleting the correct elements.
        for index in reversed(removal_indexes):
            del self._locations[index]

    # The truncate method also has a postcondition that there must be at least two locations after the method has finished executing.
    # @postcondition(at_least_two_locations) can be removed as @invariant(at_least_two_locations) already covers it 
    def truncate_at(self, name):
        # stop the itinerary at a particular location which then removes subsequent location(s)
        stop = None
        for index, location in enumerate(self._locations):
            if location.name == name:
                stop = index + 1

        self._locations = self._locations[:stop]

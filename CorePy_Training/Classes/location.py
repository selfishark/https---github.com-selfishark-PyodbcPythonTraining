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
    print(f"Decorating {cls.__name__} with auto_repr")
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

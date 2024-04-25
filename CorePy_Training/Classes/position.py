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
            component_format_spec = f".{num_decimal_places}f" # convert the suffix to a format specifier, .{num_decimal_places}f

        latitude = format(abs(self.latitude), component_format_spec)   # convert latitude to the assigned a format specifier, component_format_spec
        longitude = format(abs(self.longitude), component_format_spec)  # convert latitude to the assigned a format specifier, component_format_spec
        return (f"{latitude}° {self.latitude_hemisphere}, "
                f"{longitude}° {self.longitude_hemisphere}")

class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass


def typename(obj):
    # type(obj).__name__ is used to dynamically retrieve the name of the current object (at runtime) to avoid confusion in case of inheritance
    return type(obj).__name__

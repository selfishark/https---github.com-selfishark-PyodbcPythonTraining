from dataclasses import dataclass # from standard library
from position import Position, EarthPosition


# classes without invariant properties are not much more than dictionaries and so the marginal value of a data class mechanism is eroded.

@dataclass(eq=True, frozen=True)     # repr=True, order=False, init=True, unsafe_hash=False are other parameters that can be passed to dataclass to initialize the class
class Location:
    # here the data type declaration helps dataclass to know which attribute is required
    # the dataclass decorator will automatically generate the __init__ method
    # it is then going to collect the attributes name and position to synthesize the __repr__ method
    # eq will be called with the attribute name and position to compare them to two other objects to check if they are equal, see position.py
    # frozen will be called to generate a hash value for the object to be used in a dictionary lookup function, see position.py
    # keep dataclasses simple, avoid combining them with inheritance, stick to the basic options and exhibit a strong preference for immutability.
    name: str
    position: Position

    def __post_init__(self):
        # post_init can get hold of everything it needs through self
        # post_init is used to validate the object's state after the __init__ method has been called
        # it is perfect to perform validation on data class instances construction
        if self.name == "":
            raise ValueError("Location name cannot be empty")


hong_kong = Location("Hong Kong", EarthPosition(22.29, 114.16))
stockholm = Location("Stockholm", EarthPosition(59.33, 18.06))
cape_town = Location("Cape Town", EarthPosition(-33.93, 18.42))
rotterdam = Location("Rotterdam", EarthPosition(51.96, 4.47))
maracaibo = Location("Maracaibo", EarthPosition(10.65, -71.65))

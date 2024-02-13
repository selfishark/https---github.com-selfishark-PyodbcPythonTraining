class ShippingContainer:

    # Class attribute that is used to give a unique serial number to each instance.
    # This line initializes the class attribute next_serial with the value 1337. 
    # This attribute is shared among all instances of the ShippingContainer class.
    next_serial = 1337

    def __init__(self, owner_code, contents):
        # Instance attribute for owner code
        self.owner_code = owner_code
        # Instance attribute for contents
        self.contents = contents

        # Assign the current value of next_serial to the serial attribute of the instance
        # Inside the __init__ method, this line assigns the current value of next_serial to the serial attribute of the newly created instance. 
        # This gives the instance a unique serial number.
        self.serial = ShippingContainer.next_serial     # Use ShippingContainer. instead of self. to distinguish between class and instance attributes;
                                                        # besides, using self. creates another attribute instance which would hide the class attribute and the class will remain unmodified

        # Increment next_serial by 1 to ensure the next instance gets a different serial number
        # This line increments next_serial by 1. 
        # This ensures that the next instance of ShippingContainer will get a different serial number.
        ShippingContainer.next_serial += 1              # another remark why using ShippingContainer. instead of self.: instance attributes takes precedence over class attributes, when read through self;

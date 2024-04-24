class ShippingContainer:

    # Class attribute that is used to give a unique serial number to each instance.
    # This line initializes the class attribute next_serial with the value 1337. 
    # This attribute is shared among all instances of the ShippingContainer class.
    next_serial = 1337

    @classmethod   # this decorator is used to bind the _generate_serial method to the ShippingContainer class and not the instance
    def _generate_serial(cls):  # use 'cls' argument to the class object ShippingContainer 
        result = cls.next_serial

        # Increment next_serial by 1 to ensure the next instance gets a different serial number
        # This ensures that the next instance of ShippingContainer will get a different serial number.
        cls.next_serial += 1  # cls is used instead of ShippingContainer to make the method more flexible and easier to maintain
        return result

    def __init__(self, owner_code, contents):
        # Instance attribute for owner code
        self.owner_code = owner_code
        # Instance attribute for contents
        self.contents = contents

        # Assign the current value of next_serial to the serial attribute of the instance
        # Inside the __init__ method, this line assigns the current value of next_serial to the serial attribute of the newly created instance.
        # This gives the instance a unique serial number.
        self.serial = ShippingContainer._generate_serial()  # we keep ShippingContainer. instead of cls. because when ShippingContainer._generate_serial() is invoked it refers to the classmethod directly

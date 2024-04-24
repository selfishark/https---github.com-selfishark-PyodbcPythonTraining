import iso6346


class ShippingContainer:

    # Class attribute that is used to give a unique serial number to each instance.
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        # This method generates a unique serial number by using the current value of next_serial
        result = cls.next_serial
        cls.next_serial += 1  # Increment next_serial for the next instance
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        # This method generates a BIC code using the owner_code and serial number, with category 'U' by default
        # Changing the category to another letter could require a polymorphism overwrite for example with RefrigeratedShippingContainer
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6)
            )

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        # This method creates an empty ShippingContainer
        # A class method already behaves polymorphically
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        # This method creates a ShippingContainer with specified items
        # A class method already behaves polymorphically
        # The **kwargs allows the base class not to see what the derived class is made of
        return cls(owner_code, length_ft, contents=list(items), **kwargs)

    def __init__(self, owner_code, length_ft, contents, **kwargs):  # **kwargs allows the base class not to see what the derived class is made of
        self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        # Generate a unique serial number for this instance
        serial = ShippingContainer._generate_serial()
        # Use the owner_code and serial number to create a BIC code for this instance
        self.bic = self._make_bic_code(  # we use 'self' to allow polymorphism on static's method to work.
            owner_code=owner_code,
            serial=serial
            )

    @property
    def volume_ft3(self):
        # This function is a template method, it does not do any calculation;
        # It just delegates the calculation to the _calc_volume method which could be easily be overridden in a derived class.
        return self._calc_volume()

    def _calc_volume(self):
        # This method calculates the volume of the container in cubic feet
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft




class RefrigeratedShippingContainer(ShippingContainer):
    # This class inherits from ShippingContainer and adds a temperature attribute
    # it uses **kwargs to avoid circular dependencies as base class should not know about their derived class
    # to avoid Class Invariant Violation we should use

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):     # using * before celsuis turns is into a kwarg
        # Call the __init__ method of the parent class using super() for explicitness initialisation inheritance
        super().__init__(owner_code, length_ft, contents, **kwargs)  # owner_code, length_ft, and contents are passed to the parent class with the buit-in super() function
        # the __init__ checks if the temperature is too high using the celsius setter @property (via self encapsulation) before assigning the value
        self.celsius = celsius
    
    @property
    def celsius(self):
        # This method returns the temperature in Celsius like an attribute due to the @property decorator
        # @property is a built-in decorator that makes a 'getter' method behave like an attribute
        # This can be considered as a read-only attribute so celsius can't be set from outside
        # the function should have the same name as the attribute, hence 'celsius' and can only be modified by the setter
        # This is an example of encapsulation, where the attribute is hidden behind a method (e.g. celsius.setter assign the value of 'celsius' to _celsius attribute rather than directly accessing it)
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        # This another template method that delegates the setting of the temperature to the _set_celsius method
        return self._set_celsius(value)
    
    def _set_celsius(self, value):
        # setter allows the attribute to be set from outside
        # the setter is a method which conventionally has the same name as the getter, decorated by the 'setter' decorator retrieved from the property object, for instance 'celsius'
        # the class invariant is checked here
        # the new value of the celsius property is set here if it meets the MAX_CELSIUS constraint to maintain the invariant check
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temperature too high!")
        self._celsius = value

    # _c_to_f and _f_to_c are good staticmethod candidates as they do not depend on the instance or class object but don't belong in the global module of ShippingContainer classes either.
    @staticmethod
    def _c_to_f(celsius):
        # This static method converts the temperature from Celsius to Fahrenheit
        return celsius * 9/5 + 32

    @staticmethod
    def _f_to_c(fahrenheit):
        # This static method converts the temperature from Fahrenheit to Celsius
        return (fahrenheit - 32) * 5/9

    @property
    def fahrenheit(self):
        # This is a getter method for the 'fahrenheit' property.
        # It returns the temperature in Fahrenheit by converting the 'celsius' attribute from Celsius to Fahrenheit using the _c_to_f static method.
        # this example shows that @property don't have to the backed up by attributes and can be computer when needed.
        return RefrigeratedShippingContainer._c_to_f(self.celsius)

    @fahrenheit.setter
    def fahrenheit(self, value):
        # This is a setter method for the 'fahrenheit' property.
        # It sets the temperature in Celsius by converting the provided Fahrenheit value to Celsius using the _f_to_c static method.
        # This way, when you set a value in Fahrenheit, the 'celsius' attribute is updated accordingly.
        self.celsius = RefrigeratedShippingContainer._f_to_c(value)

    def _calc_volume(self):
        # This method calculates the volume of the container in cubic feet
        # This method is polymorphic with the base class method, but it is not overwritten here
        # This is an example of polymorphism where the method is inherited from the base class
        return super()._calc_volume() - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3

    @staticmethod
    def _make_bic_code(owner_code, serial):
        # This method generates a BIC code using the owner_code and serial number, with category 'R' for refrigerated containers
        # Polymorphism with inheritance means that the version of a method called will depend on the type of object on which it is invoked.
        # Although the polymorphism overwrite works only if called on an instance of the class (through self).
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
            )


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):
    MIN_CELSIUS = -20.0

    def _set_celsius(self, value):
        # This setter method overrides the setter method of the parent class
        # It checks if the temperature is too low using the MIN_CELSIUS class attribute before assigning the value
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temperature too low!")
        # The super() function is used to call the setter method of the parent class explicitly
        #super(HeatedRefrigeratedShippingContainer, HeatedRefrigeratedShippingContainer).celsius.__set__(self, value) # This is the same as the line below, but more explicit
        #RefrigeratedShippingContainer.celsius.fset(self, value)  # This is the same as the line above, but more explicit
        super()._set_celsius(value)

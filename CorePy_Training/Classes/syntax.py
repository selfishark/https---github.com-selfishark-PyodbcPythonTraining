"""
Usage:
    obj = MyClass("I'm an instance attribute")
    print(MyClass.class_attribute)  # Accessing class attribute
    print(obj.instance_attribute)  # Accessing instance attribute
"""


class MyClass:
    """
    This is MyClass which demonstrates class and instance attributes.
    """
    MY_CLASS_ATTRIBUTES = 'here goes class attributes'
    MY_CONSTANT = 'here goes class constant'

    def __init__(self, value):
        """
        Initialize MyClass with a attribute.
        """
        self.instance_attribute = value  # This is an instance attribute

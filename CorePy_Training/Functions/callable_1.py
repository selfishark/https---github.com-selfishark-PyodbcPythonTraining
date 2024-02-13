class ValueCalculator:
    """
    A class that encapsulates the value calculation functionality.
    In this example the ValueCalculator class has the __call__ method, 
    which allows instances of the class to be called as if they were functions. 
    This way, you can create an instance of ValueCalculator and use it as a callable to perform the value calculations.
    """

    def __init__(self):
        pass

    def eng2(self, r):
        """
        Calculate the result of 0.7724 multiplied by the input parameter 'r' and then multiplied by 1.0134.

        :param r: A numeric value.
        :return: The result of the calculation.
        """
        return 0.7724 * r * 1.0134

    def next100(self, n):
        """
        Round the input parameter 'n' to the nearest multiple of 100.

        :param n: A numeric value.
        :return: The rounded result to the nearest multiple of 100.
        """
        return int(round(n, -2))

    def __call__(self, tach):
        """
        Calculate and return a list of rounded values by applying the 'eng2' and 'next100' functions.

        :param tach: A range of values.
        :return: A list of rounded values.
        """
        # Apply 'eng2' to each element in the 'tach' range
        eng2_results = map(self.eng2, tach)

        # Apply 'next100' to round each result to the nearest multiple of 100
        rounded_values = list(map(self.next100, eng2_results))

        return rounded_values


# Example usage:
if __name__ == "__main__":
    # Create an instance of the ValueCalculator class
    calculator = ValueCalculator()

    # Define the 'tach' range and use the instance as a callable
    result_list = calculator(range(1100, 3500, 200))

    # Print the result
    print(result_list)

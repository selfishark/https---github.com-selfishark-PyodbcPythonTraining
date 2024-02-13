# class Engine:
#     def __init__(self):
#         self.cache = {}

#     @staticmethod
#     def next100(x: float) -> int:
#         return int (round(x, 2))

#     def __call__(self, tach: float) -> int:
#         t100 = self.next100(tach)
#         if t100 not in self.cache:
#             actual = self.next100(0.7724*t100**1.0134)
#             self.cache[t100] = actual
#         return self.cache[t100]

class Engine:
    def __init__(self):
        """
        Initialize the Engine instance with an empty cache.
        """
        self.cache = {}

    @staticmethod
    def next100(x: float) -> int:
        """
        Round the input parameter 'x' to the nearest multiple of 100.

        :param x: A numeric value.
        :return: The rounded result to the nearest multiple of 100.
        """
        return int(round(x, -2))

    def __call__(self, tach: float) -> int:
        """
        Calculate and return a result based on the 'tach' parameter, caching the calculated values.

        :param tach: A numeric value.
        :return: The calculated result.
        """
        t100 = self.next100(tach)

        if t100 not in self.cache:
            # Perform the calculation and round the result to the nearest multiple of 100
            actual = self.next100(0.7724 * t100**1.0134)
            
            # Cache the result
            self.cache[t100] = actual

        # Return the cached result
        return self.cache[t100]


# Example usage:
if __name__ == "__main__":
    # Create an instance of the Engine class
    engine = Engine()

    # Define the range of 'tach' values
    tach_values = range(1100, 3500, 200)

    # Loop over each 'tach' value and execute the Engine instance
    for tach_value in tach_values:
        result = engine(tach_value)
        print(f"tach: {tach_value}, result: {result}")

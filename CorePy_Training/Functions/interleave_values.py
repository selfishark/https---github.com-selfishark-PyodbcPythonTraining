# def eng2(r):
#     return 0.7724*r*1.0134


# def next100(n):
#     return int(round(n, -2))


# tach = range(1100, 3500, 200)
# a = list(map(next100, map(eng2, tach)))

# print(a)

def eng2(r):
    """
    Calculate the result of 0.7724 multiplied by the input parameter 'r' and then multiplied by 1.0134.

    :param r: A numeric value.
    :return: The result of the calculation.
    """
    return 0.7724 * r * 1.0134  


def next100(n):
    """
    Round the input parameter 'n' to the nearest multiple of 100.

    :param n: A numeric value.
    :return: The rounded result to the nearest multiple of 100.
    """
    return int(round(n, -2))


def calculate_rounded_values(tach):
    """
    Calculate and return a list of rounded values by applying the 'eng2' and 'next100' functions.

    :param tach: A range of values.
    :return: A list of rounded values.
    """
    # Apply 'eng2' to each element in the 'tach' range
    eng2_results = map(eng2, tach)

    # Apply 'next100' to round each result to the nearest multiple of 100
    rounded_values = list(map(next100, eng2_results))

    return rounded_values


# Example usage:
if __name__ == "__main__":
    from pprint import pprint
    # Define the 'tach' range
    tach_range = range(1100, 3500, 200) # range of values from 1100 to 3500 with a step of 200

    # Calculate rounded values
    result_list = calculate_rounded_values(tach_range)

    # Zipping the result
    zip_result = list(zip(tach_range, result_list))

    # Lambda function
    lambda_result = list(zip(map(lambda r: 0.7724 * r * 1.0134, tach_range)))

    # Print the result
    print(result_list)
    pprint(zip_result)


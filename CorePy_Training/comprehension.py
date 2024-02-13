from pprint import pprint as pp


country_to_capital = {"UK": "London", "US": "New York", "CY": "Nicosia", "CZ": "Prague"}

capital_to_country = {
    capital: country for country, capital in country_to_capital.items()
}


pp(capital_to_country)

################################

words = ["English", "French", "German", "Spanish", "Mandarin", "Latin"]
first_letter = {x[0]: x for x in words}
pp(first_letter)

################################

from math import sqrt


# Function to check if a number is prime
def is_prime(x):
    # Numbers less than 2 are not prime
    if x < 2:
        return False
    
    # Check divisors from 2 to the square root of x
    for i in range(2, int(sqrt(x)) + 1):
        # If x is divisible evenly by i, it's not prime
        if x % i == 0:
            return False
    
    # If no divisors are found, x is prime
    return True


# List comprehension to generate a list of prime numbers from 0 to 100
result_prime = [x for x in range(101) if is_prime(x)]   # comprehension expression should have any side-effect (i.e. print statement)

# Print the result using the function pp
pp(result_prime)

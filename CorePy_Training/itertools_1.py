# itertools is an open-ended version of range more powerful than range
# contains: islice() and count(); any() and all(); zip()

from math import sqrt
from itertools import islice, count, chain
from pprint import pprint as pp


################################ islice() and count() 

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


thousand_primes = islice((x for x in count() if is_prime(x)), 1000) # slice () produce the first 1000 prime numbers
                                                                    # count() generates infinite sequence of numbers 
                                                                    # is_prime(x) filters only the prime numbers
prime_list = list(thousand_primes)[-10:]                            # [-10:] takes the last 10 elements of the list
sum_list = list(prime_list) 
print(f"{prime_list} \n {sum(sum_list)}")



################################  any() and all()

    ## Check if any number in the range between the first and third element of prime_list is prime
is_any= any(is_prime(x) for x in range(prime_list[0], prime_list[2]))
print(is_any)

    ## Check if all words in the list are capitalized (title case)
words = ["English", "french", "German", "Spanish", "Mandarin", "Latin"]

is_all = all(name == name.title() for name in words)    #checks if each word in the list is in title case.
print(is_all)



################################  zip()
    # takes two or more iterables and returns an iterator that generates tuples containing elements from the input iterables
    # takes multiple iterables and returns an iterator that generates elements from the first iterable until it's exhausted


# Temperature data for three days
monday = [138, 23, 49, 289, 46, 52, 35]
tuesday = [89, 65, 332, 214, 321, 56, 52]
wednesday = [65, 34, 78, 45, 164, 321, 54]

# Calculate and print the average of each pair of temperatures from Monday and Tuesday
for m, t in zip(monday, tuesday):
    print("avg_m+t =", (m + t) / 2)

# Calculate and print the min, max, and average temperatures for each corresponding time slot over the three days
for temps in zip(monday, tuesday, wednesday):               # combines iterables element-wise into tuples, creating an iterator of tuples.
    min_t = min(temps)
    max_t = max(temps)
    avg_t = sum(temps)/len(temps)
    pp(f"min = {min_t}:4.1f, max={max_t}:4.1f, avg={avg_t}4.1f")

# Chain all the temperatures into a single iterable
temperatures = chain(monday, tuesday, wednesday)            # concatenates iterables, creating a single flattened iterable
is_all_chained = all(temp > 0 for temp in temperatures)     # Check if all temperatures in the chained iterable are greater than 0

print(is_all_chained)

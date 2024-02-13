from functools import reduce


def count_words(doc):
    """
    This function takes a string (a document) as an argument 
    and returns a dictionary where the keys are words and the values are the number of times each word appears in the document.
    """
    # Normalize the document by converting it to lowercase and replacing non-alphabetic characters with spaces
    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    # Split the normalized document into words and count the frequency of each word
    for word in normalised_doc.split():

        # Inside the loop, this line updates the count of the current word in the frequencies dictionary. 
        # If the word is already a key in the dictionary, frequencies.get(word, 0) returns its current count; if the word is not a key in the dictionary, frequencies.get(word, 0) returns 0. 
        # Then, 1 is added to this value to account for the current occurrence of the word. 
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


# Test the 'count_words' function with a sample document
results = count_words('This is a sample document to test the frequency of each word in the document.')
print(results)

# Define a list of documents
document = [
    'It was the best of times, it was the worst of times.',
    'It was the age of wisdom, it was the age of foolishness.',
    'It was the epoch of belief, it was the epoch of incredulity.',
    'It was the season of Light, it was the season of Darkness.',
    'It was the spring of hope, it was the winter of despair.',
    'We had everything before us, we had nothing before us.',
    'We were all going direct to Heaven, we were all going direct the other way.',
    'In short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only.'
    ]

# Use 'map()' to apply 'count_words' to each document in the list
# This returns an iterable of dictionaries where the keys are words and the values are the number of times each word appears in each document
counts = map(count_words, document)


def combine_counts(d1, d2):
    """
    This function takes function takes two dictionaries as arguments, d1 and d2. 
    These dictionaries are expected to have words as keys and their counts as values. 
    The function combines the counts of each word from both dictionaries and returns a new dictionary with the combined counts..
    """
    # Copy the first dictionary to avoid modifying it
    d = d1.copy()

    # For each word in the second dictionary, add its count to the count in the first dictionary
    # This starts a loop that iterates over each key-value pair in the second dictionary d2. 
    # In each iteration, word is a key from d2 (a word), and count is the corresponding value (the count of that word).
    for word, count in d2.items():

        # This line updates the count of word in the dictionary d. If word is already a key in d, d.get(word, 0) returns its current count;
        # if word is not a key in d, d.get(word, 0) returns 0. Then, count (the count of word in d2) is added to this value.
        # The result is the combined count of word in both d1 and d2, and this is set as the new value of word in d.
        d[word] = d.get(word, 0) + count

    # After all key-value pairs in d2 have been processed, 
    # the function returns d, which is a dictionary that combines the counts of each word in d1 and d2.
    return d


# Use 'reduce()' to combine the dictionaries returned by 'map()'
# This returns a single dictionary that combines the counts of each word in all documents
total_counts = reduce(combine_counts, counts)

# Print the combined counts
print(total_counts)

"""
Summary:
    Module to retrieve and print from a URL.

Usage:
    python3 words.py <url_link>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Retrieve words from urlopen.

    Args:
        url: url to fetch utf-8 text file

    Returns:
        story_words: list of story words
    """
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    """Words printing function, one item per line.

    Args:
        items (list): list of words items to print
    """
    for item in items:
        print(item)


def main(url):
    """Print items in a given url.

        Args:
            url (str): url of an utf-8 text file
    """
    words = fetch_words(url)    # fetch words
    print_items(words)          # print words


if __name__ == "__main__":
    main(sys.argv[1])           # start argument list at 1; 0th being module filename

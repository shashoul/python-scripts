"""Retrieve ans print words from a URL.

Usage:
    python3 words.py <URL>
"""


import sys
from urllib.request import urlopen


def fetch_words(url):
    """ Fetch a List of words from a URL.

    Args: 
        url: the URL of a UTF-8 text document.

    Return:
        A list of strings containing the words from the document.
    """
    #story = urlopen("http://sixty-north.com/c/t.txt")
    story = urlopen(url)
    story_words = [] 
    for line in story:
        story_words += line.decode('utf-8').split()

    story.close()
    return story_words


def print_words(story_words):
    """Print words from giving list of words

    Args: 
        story_words: a list of string.
    """
    print(story_words)


def main(url):
    story_words = fetch_words(url)
    print_words(story_words)


if __name__ == "__main__":
    main(sys.argv[1])
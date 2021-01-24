"""Retrieve and print words from URL.

Usage:
    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from URL.
        
        Args: 
            url: The URL of UTF-8 text document.

        Returns:
            A list of string containing  the words from the 
            document. 
    """
    story = urlopen(url)
    story_words = []
    
    for line in story:
        line_words = line.decode('utf8').split()
        #story_words = story_words + line_words
        for word in line_words:
            story_words.append(word)
    
    story.close()
    return story_words


def print_items(items):
    """Print items one per line

        Args: 
            An iterable series of printable items. 
    """
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1])
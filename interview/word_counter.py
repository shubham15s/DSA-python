from collections import Counter
import re

def count_word_occurrences(paragraph):
    paragraph = paragraph.lower()

    words = re.findall(r'\b\w+\b', paragraph)
    word_count = Counter(words)
    for word, count in word_count.items():
        print(f"'{word}' occurs {count} times")

        
paragraph = """
This is a test. This test is only a test. In the event of an actual emergency, this would be followed by official information.
"""

count_word_occurrences(paragraph)
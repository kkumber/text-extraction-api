import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return len(words)
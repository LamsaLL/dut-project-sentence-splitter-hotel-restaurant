import os
from json import load
from difflib import SequenceMatcher

class Keyword:
    """Keyword fetcher class"""

    def __init__(self):
        """Init method"""

        self.keywords = self.load_keywords("keywords.json")


    def load_keywords(self, filename):
        """Load content from file"""

        with open(filename, "rb") as f:
            return load(f, encoding="utf-8")


    def get_keywords(self, sentence):
        """Find important words in a string
        in function of the keywords list"""

        text_keywords = []

        for w in sentence.split(" "):
            for kw in self.keywords:
                if SequenceMatcher(a=kw, b=w).ratio() > 0.90:
                    text_keywords.append(kw)
                    break

        return text_keywords

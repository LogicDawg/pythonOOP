import random
"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """finding random words from dictionary.
        >>> wf = WordFinder("words.txt")
    3 words read
    
        >>> wf.random() in ["food", "lost", "porcupine"]
    True

    >>> wf.random() in ["food", "dog", "porcupine"]
    True
    """
    def __init__(self, file):
        """Read dictionary and reports # items read."""

        dict_file = open(file)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file -> list of words."""

        return [word.strip() for word in dict_file]

    def random(self):
        """Return random word."""

        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

        >>> swf = SpecialWordFinder("words.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    

import re


class Corpus:
    def __init__(self, text: str) -> None:
        """Initialize a Corpus object with a given text."""
        self.text = text

    def clean_text(self, text: str) -> str:
        """Return a cleaned text, i.e. all lower case, no punctuation"""
        ponctuation = ['.', ',', '!', '?', ':', ';', "“", "”"]
        self.text = self.text.lower()
        text = ''.join([c for c in text if c not in ponctuation])
        text = text.replace('“', '').replace('”', '')
        return text

    def number_of_words(self) -> int:
        """Return the number of words in the text."""
        return len(self.text.split())

    def number_of_sentences(self) -> int: # Needs to be improved using regex
        """Return the number of sentences in the text."""
        return len(self.text.split('.'))

    def unique_words(self) -> tuple:
        """Return the number of unique words and a set of unique words in the text."""
        return len(set(self.text.split())), set(self.text.split())

    def word_occurance(self, word) -> tuple:
        """Return the absolute and relative frequency of a word in the text."""
        absolute = self.text.count(word)
        relative = absolute / len(self.text.split())
        return absolute, relative

    def random_word(self) -> tuple:
        """Return a random word and its absolute and relative frequency."""
        import random
        words = self.text.split()
        random_word = random.choice(words)
        return random_word, self.word_occurance(random_word)

    def write_unique_word_frequency(self) -> str:
        """Writes all unique words, how often they absolutely and relatively
        occur (ordered descending as json object strings) to a given filepath, returning the absolute
        path string to the written file."""
        import json
        from pathlib import Path
        unique_words = self.unique_words()[1]
        word_dict = {}
        for word in unique_words:
            word_dict[word] = self.word_occurance(word)
        word_dict = sorted(word_dict.items(), key=lambda x: x[1][0], reverse=True)
        
        with open(Path('unique_word_frequency.json'), 'w') as f:
            json.dump(word_dict, f, indent=4)
        return Path('unique_word_frequency.json').absolute()


    def word_length(self) -> tuple:
        """Return the maximum, minimum, and average word length."""
        text = self.clean_text(self.text)
        words = text.split()
        max_length = max([len(word) for word in words])
        min_length = min([len(word) for word in words])
        average_length = sum([len(word) for word in words]) / len(words)
        return max_length, min_length, average_length

    def vocabulary(self) -> tuple:
        """Return the vocabulary of the text, i.e. all unique characters"""
        text = self.text.lower()
        with_symbols = set(text)
        without_symbols = set([c for c in text if c.isalpha()])
        return with_symbols, without_symbols

    def starting(self, char: str) -> list:
        """Return all words starting with a given character."""
        text = self.clean_text(self.text)
        words = text.split()
        start = [word for word in words if word[0] == char]
        return start

    def ending(self, char:str) -> list:
        """Return all words ending with a given character."""
        text = self.clean_text(self.text)
        words = text.split()
        end = [word for word in words if word[-1] == char]
        return end

    def containing(self, substing: str) -> list:
        """Return all words containing a given substring."""
        text = self.clean_text(self.text)
        words = text.split()
        contain = [word for word in words if substing in word]
        return contain

    def most_frequent(self) -> str:
        """Return the most frequent word in the text."""
        text = self.clean_text(self.text)
        words = text.split()
        return max(set(words), key=words.count)

    def most_frequent_substring_length_4(self) -> str:
        """Return the most frequent substring of length 4 in the text."""
        text = self.clean_text(self.text)
        words = text.split()
        substring = [
            word[i:i + 4] for word in words for i in range(len(word) - 3)
        ]
        return max(set(substring), key=substring.count)

    def find_substring(self, substring: str):
        """Return a list of tuples, where the first element is a boolean"""
        substring_length = len(substring)
        position = [(True,
                     i) if self.text[i:i + substring_length] == substring else
                    (False, None)
                    for i in range(len(self.text) - substring_length)]
        return position

    def most_and_least_occurences(self) -> tuple:
        """Return the most and least frequent characters in the text."""
        text = self.clean_text(self.text)
        words = list(text.replace(' ', ''))

        most_frequent = max(set(words), key=words.count)
        least_frequent = min(set(words), key=words.count)
        return most_frequent, least_frequent

    def is_anagram(self, word1: str, word2: str, case_sensitive=False) -> bool:
        """Return True if two words are anagrams, False otherwise."""
        if not case_sensitive:
            word1 = word1.lower()
            word2 = word2.lower()
        return sorted(word1) == sorted(word2)

    def sentences(self) -> list:
        """Return a list of sentences in the text."""
        split_pattern = r'(?<=[.!?])\s+|(?<=[.!?][^\S\r\n]+)\n+(?=[^\W\d_]|$)(?<!\b(?:etc|i\.e|e\.g)\.)'
        sentences = re.split(split_pattern, self.text)
        return sentences

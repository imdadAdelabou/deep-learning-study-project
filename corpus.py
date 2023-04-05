import re
class Corpus:
    def __init__(self, text):
        self.text = text

    def clean_text(self, text):
        ponctuation = ['.', ',', '!', '?', ':', ';', "“", "”"]
        self.text = self.text.lower()
        text = ''.join([c for c in text if c not in ponctuation])
        text = text.replace('“', '').replace('”', '')
        return text

    def number_of_words(self):
        return len(self.text.split())

    def number_of_sentences(self):
        return len(self.text.split('.'))

    def number_of_unique_words(self):
        return len(set(self.text.split()))

    def word_length(self):
        text = self.clean_text(self.text)
        words = text.split()
        max_length = max([len(word) for word in words])
        min_length = min([len(word) for word in words])
        average_length = sum([len(word) for word in words]) / len(words)
        return max_length, min_length, average_length

    def vocabulary(self):
        text = self.text.lower()
        with_symbols = set(text)
        without_symbols = set([c for c in text if c.isalpha()])
        return with_symbols, without_symbols

    def starting(self, char):
        text = self.clean_text(self.text)
        words = text.split()
        start = [word for word in words if word[0] == char]
        return start

    def ending(self, char):
        text = self.clean_text(self.text)
        words = text.split()
        end = [word for word in words if word[-1] == char]
        return end

    def containing(self, substing):
        text = self.clean_text(self.text)
        words = text.split()
        contain = [word for word in words if substing in word]
        return contain

    def most_frequent(self):
        text = self.clean_text(self.text)
        words = text.split()
        return max(set(words), key=words.count)

    def most_frequent_substring_length_4(self):
        text = self.clean_text(self.text)
        words = text.split()
        substring = [
            word[i:i + 4] for word in words for i in range(len(word) - 3)
        ]
        return max(set(substring), key=substring.count)

    def find_substring(self, substring):
        substring_length = len(substring)
        position = [(True,
                     i) if self.text[i:i + substring_length] == substring else
                    (False, None)
                    for i in range(len(self.text) - substring_length)]
        return position

    def most_and_least_occurences(self):
        text = self.clean_text(self.text)
        words = list(text.replace(' ', ''))

        most_frequent = max(set(words), key=words.count)
        least_frequent = min(set(words), key=words.count)
        return most_frequent, least_frequent

    def is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2)

    def sentences(self):
        # Exclude decimal numbers, domain names, and abbreviations from the split pattern
        split_pattern = r'(?<!\d\.)\s*[.!?]+\s+(?!\w)|(?<=\w)\.(?=\w)(?<!etc\.)'
        sentences = re.split(split_pattern, self.text)
        return sentences

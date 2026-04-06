class StringParser:
    def __init__(self, input_string):
        self.input_string = input_string
    def remove_whitespace(self):
        return self.input_string.replace(" ", "")
    def to_uppercase(self):
        return self.input_string.upper()
    def to_lowercase(self):
        return self.input_string.lower()
    def reverse_string(self):
        return self.input_string[::-1]
    def count_characters(self):
        return len(self.input_string)
    def count_words(self):
        return len(self.input_string.split())
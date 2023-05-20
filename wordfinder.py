"""Word Finder: finds random words from a dictionary."""

class WordFinder:
    """Machine to pull random words from a text file."""
    def __init__(self, file_path):
        self.file_path = file_path
        self.words = []
        self.read_words(file_path)
    
    def read_words(self, file_path):
        with open(file_path, "r") as file:
            self.words = [word.strip() for word in file]
        print(f"{len(self.words)} words read")
        
    def random(self):
        import random
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Special use case of WordFinder to get around text files with blank lines/# character"""
    def __init__(self, file_path):
        super().__init__(file_path)
        self.word_filter()
    
    def word_filter(self):
        filtered_words = []
        for word in self.words:
            if not word.startswith("#") and word.strip() != "":
                filtered_words.append(word)
        self.words = filtered_words
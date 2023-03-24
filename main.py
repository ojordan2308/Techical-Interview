from random import randrange

DICTIONARY = []
with open('./dictionary.txt') as dictionary:
    for line in dictionary:
        word = line.rstrip('\n')
        DICTIONARY.append(word)

letter_points = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1, "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10
}

ALPHA = 'abcdefghijklmnopqrstuvwxyz'

def calculate_score(word: str) -> int:
    """Calculate the scrabble score of a word."""
    score = 0
    for letter in word:
        score += letter_points[letter.upper()]
    
    return score

def create_bag() -> list:
    """Generates bag of scrabble tiles"""
    return ['E'] * 12 + \
           (['A'] + ['I']) * 9 + \
           ['O'] * 8 + \
           (['N'] + ['R'] + ['T']) * 6 + \
           (['L'] + ['S'] + ['U'] + ['D']) * 4 + \
           ['G'] * 3 + \
           (['B'] + ['C'] + ['M'] + ['P'] + ['F'] + ['H'] + ['V'] + ['W'] + ['Y']) * 2 + \
           (['K'] + ['J'] + ['X'] + ['Q'] + ['Z'])
    
BAG = create_bag()

def assign_letters() -> str:
    """Assigns 7 random letters for a player."""
    result = ''
    for i in range(7):
        result += BAG.pop(randrange(0, len(BAG)-1))
    return result

def find_word(rack: str) -> str:
    """Finds valid word from rack."""
    valid_words = []
    for word in DICTIONARY:
        valid_word = True
        for letter in word:
            count = word.count(letter)
            if rack.count(letter) >= count:
                continue
            else:
                valid_word = False
        if valid_word:
            valid_words.append(word)

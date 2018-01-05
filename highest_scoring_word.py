"""Kata: Highest Scoring Word
Given a string of words, find the highest scoring word.
Each letter of a word scores points according to it's position in the alphabet
Rreturn the highest scoring word as a string."""


def high(string):
    """function takes in a string, splits it, and finds one with largest value."""
    word_list = string.split()
    letters = []
    word_dict = {}
    for word in word_list:
        string_list = [x for x in word]
        word_sum = 0
        for letter in string_list:
            word_sum += ord(letter) - 97
        word_dict[word] = word_sum
    return max(word_dict, key=lambda key: word_dict[key])
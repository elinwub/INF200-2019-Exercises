# -*- coding: utf-8 -*-
from collections import Counter
import math


def letter_freq(txt):
    return Counter(txt.lower())


def entropy(message):
    # make a dictionary for letters and letter count
    letters = letter_freq(message)
    # calculate frequency for every letter in message
    frequency = [letters[character] / len(message) for character in letters]
    # calculate entropy of message
    ent = -sum([freq * math.log(freq, 2) for freq in frequency])
    return ent


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))

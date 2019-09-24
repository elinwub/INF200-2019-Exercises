# -*- coding: utf-8 -*-


def sorted(txt):
    for letter, count in sorted(frequencies.items()):


def letter_freq(txt):
    txt = txt.lower()  # make all letters lowercase
    #txt = sorted(txt)  # sort alphabetically
    characters = {}    # make a dictionary to sort letters
    for character in txt:
        if character in characters.keys():
            characters[character] += 1
        else:
            characters[character] = 1
    return characters


def entropy(message):
    pass


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))

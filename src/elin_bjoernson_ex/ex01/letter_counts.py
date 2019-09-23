# -*- coding: utf-8 -*-
def letter_freq(txt):
    txt = txt.lower()  # make all letters lowercase
    txt = sorted(txt)  # sort alphabetically
    characters = {}    # make a dictionary to sort letters
    for character in txt:
        if character in characters.keys():
            characters[character] += 1
        else:
            characters[character] = 1
    return characters


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))

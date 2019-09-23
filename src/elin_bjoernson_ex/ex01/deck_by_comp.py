# -*- coding: utf-8 -*-


SUITS = ('C', 'S', 'H', 'D')
VALUES = range(1, 14)


def deck_loop():
    deck = []
    for suit in SUITS:
        for val in VALUES:
            deck.append((suit, val))
    return deck


def deck_comp():
    deck = [(s, v) for s, v in [(s, v) for s in SUITS for v in VALUES]]
    return deck


if __name__ == '__main__':
    if deck_loop() != deck_comp():
        print('ERROR!')

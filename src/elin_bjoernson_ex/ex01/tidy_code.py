# -*- coding: utf-8 -*-
from random import randint

__author__ = 'Elin Bjoernson'
__email__ = 'elinbj@nmbu.no'


def guess_number():
    number = 0
    while number < 1:
        number = int(input('Your guess: '))
    return number


def random_number():
    return randint(1, 6) + randint(1, 6)


def same_value(f, g):
    return f == g


if __name__ == '__main__':

    correct_guess = False
    attempts = 3
    correct_number = random_number()
    while not correct_guess and attempts > 0:
        guess = guess_number()
        correct_guess = same_value(correct_number, guess)
        if correct_guess is False:
            print('Wrong, try again!')
            attempts -= 1

    if attempts > 0:
        print('You won {} points.'.format(attempts))
    else:
        print('You lost. Correct answer: {}.'.format(correct_number))

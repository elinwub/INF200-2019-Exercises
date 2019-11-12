# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Elin Wølner Bjørnson'
__email__ = 'jaer@nmbu.no', 'elinbj@nmbu.no'


class Board:
    std_ladders = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    std_chutes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    std_goal = 90

    def __init__(self, ladders, chutes, goal):
        self.ladders = None
        self.chutes = None
        self.goal = None

        if ladders & chutes & goal is not None:
            self.ladders = ladders
            self.chutes = chutes
            self.goal = goal

        else:
            self.ladders = Board.std_ladders
            self.chutes = Board.std_chutes
            self.goal = Board.std_goal





# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Elin Wølner Bjørnson'
__email__ = 'jaer@nmbu.no', 'elinbj@nmbu.no'


class Board:
    std_board = {}

    def __init__(self, ladders, chutes, goal):
        self.ladders = None
        self.chutes = None
        self.goal = None
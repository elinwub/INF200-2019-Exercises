# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Elin Wølner Bjørnson'
__email__ = 'jaer@nmbu.no', 'elinbj@nmbu.no'

from random import randint


class Board:
    std_goal = 90
    std_board = {1 : 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                 24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    def __init__(self, ladders, chutes, goal):
        self.ladders = None
        self.chutes = None
        self.goal = None

        if ladders & chutes & goal is not None:
            self.board = {**dict(ladders), **dict(chutes)}
            self.goal = goal

        else:
            self.board = Board.std_board
            self.goal = Board.std_goal

    def goal_reached(self, position):
        return position >= self.goal

    def position_adjustment(self, position):
        return self.board.get(position, position) - position


class Player:
    def __init__(self, board):
        self.board = board
        self.position = 0

    def move(self):
        self.position += randint(1, 6)
        self.position += self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board, extra_steps=1):
        super().__init__(board)
        self.extra_steps = extra_steps
        self.is_chute = False

    def move(self):
        self.position += randint(1, 6)

        if self.is_chute is True:
            self.position += self.extra_steps
            self.is_chute = False

        chute_ladder = self.board.position_adjustment(self.position)
        self.position += chute_ladder

        if chute_ladder < 0:
            self.is_chute = True


class LazyPlayer(Player):
    def __init__
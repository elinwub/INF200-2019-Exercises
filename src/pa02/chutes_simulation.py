# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Elin Wølner Bjørnson'
__email__ = 'jaer@nmbu.no', 'elinbj@nmbu.no'

from random import randint
import random


class Board:
    std_goal = 90
    std_board = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                 24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    def __init__(self, ladders=None, chutes=None, goal=None):

        if ladders and chutes and goal is not None:
            self.board = {**dict(ladders), **dict(chutes)}
            self.goal = goal

        else:
            self.board = Board.std_board
            self.goal = Board.std_goal

    def goal_reached(self, position):
        """
        Returns true or false if goal is reached

        Parameters
        ----------
        position

        Returns
        -------
        bool
        """
        return position >= self.goal

    def position_adjustment(self, position):
        """
        returns 'delta position' if players lands on ladder or chute
        else it will return 0

        Parameters
        ----------
        position

        Returns
        -------
        'delta position'
        """
        return self.board.get(position, position) - position


class Player:
    def __init__(self, board=Board()):
        self.board = board
        self.position = 0

    def move(self):
        """Moves according to die roll, and chute or ladder
        Changes position
        """
        self.position += randint(1, 6)
        self.position += self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board=Board(), extra_steps=1):
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
    def __init__(self, board=Board(), dropped_steps=1):
        super().__init__(board)
        self.drop_steps = dropped_steps
        self.is_ladder = False

    def move(self):
        dice = randint(1, 6)

        if self.is_ladder is True:
            if dice <= self.drop_steps:
                self.is_ladder = False
            else:
                self.position += dice - self.drop_steps
                self.is_ladder = False
        else:
            self.position += dice

        chute_ladder = self.board.position_adjustment(self.position)
        self.position += chute_ladder

        if chute_ladder > 0:
            self.is_ladder = True


class Simulation:
    def __init__(self, player_field, board=Board(), seed=1,
                 randomize_players=False):
        self.players = [p() for p in player_field]
        self.board = board
        self.seed = random.seed(seed)
        self.randomize_players = randomize_players
        self.turns = 0
        if self.randomize_players is True:
            random.shuffle(self.players)

    def single_game(self):
        """
        Runs single game, returns number of moved and the type of player who
        won
        :return:
        tuple (num_moves, 'player_type')
        """
        has_won = False

        while has_won is False:
            for player in self.players:
                self.turns += 1
                player.move()
                has_won = self.board.goal_reached(player.position)

            return self.turns, type(player).__name__
    def run_simulation(self):
        """
        Runs a given number of simulations
        """

    def get_results(self):
        """
        Returns results from run_simulation
        :return:

        """

    def winners_per_type(self):
        """

        :return:
        dictionary mapping player types to number of wins
        """

    def durations_per_type(self):
        """

        :return:
        dictionary mapping player types to lists of game durations of that type
        """

    def players_per_type(self):
        """

        :return:
        Dictionary showing how many players of each type participate
        """

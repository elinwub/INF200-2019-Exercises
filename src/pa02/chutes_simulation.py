# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Elin Wølner Bjørnson'
__email__ = 'jaer@nmbu.no', 'elinbj@nmbu.no'

from collections import defaultdict
from random import randint
import random


class Board:
    std_goal = 90
    std_board = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                 24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    def __init__(self, ladders=None, chutes=None, goal=None):
        """
        Initialise Board
        Parameters
        ----------
        ladders: dict
            positions and destinations of ladders
        chutes: dict
            positions and destinations of chutes
        goal: int
            position where the goal is reached
        """

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
        position: int

        Returns
        -------
        bool
        """
        return position >= self.goal

    def position_adjustment(self, position):
        """
        Returns 'delta(Δ) position' if players lands on ladder or chute
        else it will return 0
        Parameters
        ----------
        position: int

        Returns
        -------
        int
            delta position
        """

        return self.board.get(position, position) - position


class Player:
    def __init__(self, board=Board()):
        """
        Initialise Player
        Parameters
        ----------
        board: class
            the board used in the game.
        """
        self.board = board
        self.position = 0

    def move(self):
        """
        Moves according to die roll, and chute or ladder
        Changes position
        Returns nothing
        """
        self.position += randint(1, 6)
        self.position += self.board.position_adjustment(self.position)


class ResilientPlayer(Player):
    def __init__(self, board=Board(), extra_steps=1):
        """
        Initialise ResilientPlayer subclass
        Parameters
        ----------
        board: class
            board used in the game
        extra_steps: int
            number of extra steps to be taken after landing on chute
        """
        super().__init__(board)
        self.extra_steps = extra_steps
        self.is_chute = False

    def move(self):
        """
        Moves position according to die roll, and adding extra steps on next
        turn if player lands on chute
        Changes player position
        Returns nothing
        """
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
        """
        Initialise LazyPlayer
        Parameters
        ----------
        board: class
            Board used in the game
        dropped_steps: int
            Amount of steps dropped when landing on ladder
        """
        super().__init__(board)
        self.drop_steps = dropped_steps
        self.is_ladder = False

    def move(self):
        """
        Moves player according to die roll, dropping steps next turn if player
        lands on ladder.
        Changes player position
        Returns nothing.
        """
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
        """
        Initialise simulation
        Parameters
        ----------
        player_field: list
            List of players in game
        board: class
            Board used in game
        seed: int
        randomize_players: bool
            option to randomize order of players
        """
        self.players = player_field
        self.board = board
        self.seed = random.seed(seed)
        self.randomize_players = randomize_players
        self.turns = 0
        self.results = []
        if self.randomize_players is True:
            random.shuffle(self.players)

    def single_game(self):
        """
        Runs single game, returns number of moves and the type of player who
        won
        Returns
        -------
        tuple (num_moves, 'player_type')
        """

        players = [p(self.board) for p in self.players]
        self.turns = 0

        while True:
            self.turns += 1
            for player in players:
                player.move()
                if self.board.goal_reached(player.position):
                    return self.turns, type(player).__name__

    def run_simulation(self, n_sim):
        """
        Runs a number of simulations, adding it to results
        Parameters
        ----------
        n_sim: int
            number of simulations to be run

        Returns nothing
        """
        for _ in range(n_sim):
            self.results.append(self.single_game())

    def get_results(self):
        """
        Returns the results from run_simulation
        Returns
        -------
        list[tuples]
            List of tuples showing how many moves and which winner
        """

        return self.results

    def winners_per_type(self):
        """
        Returns dictionary mapping player types to number of wins
        Returns
        -------
        dict
        """

        winner_map = {}
        winners = [winner[1] for winner in self.results]
        for items in winners:
            winner_map[items] = winners.count(items)
        return winner_map

    def durations_per_type(self):
        """
        Returns dictionary mapping player types to lists of game durations
        of each type of player
        Returns
        -------
        dict
        """

        durations = defaultdict(list)
        for moves, player in self.get_results():
            durations[player].append(moves)

        return dict(durations)

    def players_per_type(self):
        """
        Returns dictionary showing how many players of each type participate
        in the game
        Returns
        -------
        dict
        """

        player_counter = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}
        for player in self.players:
            player_counter[player.__name__] += 1
        return player_counter

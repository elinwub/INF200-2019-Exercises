# -*- coding: utf-8 -*-

__author__ = 'Elin Wølner Bjørnson'
__email__ = 'elinbj@nmbu.no'


class Walker:
    def __init__(self, position, home):
        self.position = position
        self.home = home
        self.moves = 0

    def move(self):
        left_or_right = [-1, 1]
        self.position += random.choice(left_or_right)
        self.moves += 1

    def is_at_home(self):
        return self.position == self.home

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.moves


def walk(dist, pos, h):
    for i in range(len(dist)):
        moves = []
        for j in range(5):
            walker = Walker(pos[i], h[i])
            while not walker.is_at_home():
                walker.move()
            moves.append(walker.get_steps())
        print(f'Distance: {dist[i]} -> Path lengths: {moves}')

class Simulation():
    def __init__(self, start, home, seed):
        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """

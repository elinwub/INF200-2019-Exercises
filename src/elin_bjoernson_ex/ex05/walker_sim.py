# -*- coding: utf-8 -*-
import random

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


class Simulation:
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
        self.start = start
        self.home = home
        self.seed = seed

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        Returns
        -------
        int
            The number of steps taken
        """
        single_walker = Walker(self.start, self.home)
        while not single_walker.is_at_home():
            random.seed(self.seed)
            single_walker.move()
        return single_walker.get_steps()

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
        moves = []
        for i in range(num_walks):
            moves.append(self.single_walk())
        return moves


if __name__ == '__main__':
    sim1 = Simulation(0, 10, 12345)
    print(sim1.run_simulation(20))
    print(sim1.run_simulation(20))
    sim2 = Simulation(0, 10, 54321)
    print(sim2.run_simulation(20))
    sim3 = Simulation(10, 0, 12345)
    print(sim3.run_simulation(20))
    print(sim3.run_simulation(20))
    sim4 = Simulation(10, 0, 54321)
    print(sim2.run_simulation(20))

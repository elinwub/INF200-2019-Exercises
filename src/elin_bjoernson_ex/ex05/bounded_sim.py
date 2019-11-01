# -*- coding: utf-8 -*-
from walker_sim import Walker, Simulation
import random

__author__ = 'Elin Wølner Bjørnson'
__email__ = 'elinbj@nmbu.no'


class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):
        """
        Initialise the walker

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.left_limit = left_limit
        self.right_limit = right_limit

        super().__init__(start, home)

    def move(self):
        if self.position >= self.right_limit:
            self.position -= 1
        elif self.position <= self.left_limit:
            self.position += 1
        else:
            left_or_right = [-1, 1]
            self.position += random.choice(left_or_right)
            self.moves += 1


class BoundedSimulation(Simulation):
    def __init__(self, start, home, seed, left_limit, right_limit):
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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """
        self.left_limit = left_limit
        self.right_limit = right_limit
        self.start = start
        self.home = home
        self.seed = seed

        super().__init__(start, home, seed)

    def single_walk(self):
        single_walker = BoundedWalker(self.start, self.home, self.left_limit, self.right_limit)
        while not single_walker.is_at_home():
            random.seed(self.seed)
            single_walker.move()
        return single_walker.get_steps()

    def run_simulation(self, num_walks):
        moves = []
        for i in range(num_walks):
            walker = BoundedWalker(self.start, self.home, self.left_limit, self.right_limit)
            while not walker.is_at_home():
                random.seed(self.seed)
                walker.move()
            moves.append(walker.get_steps())
        return moves


if __name__ == '__main__':
    sim1 = BoundedSimulation(0, 10, 54321, -1, 11)
    print(sim1.run_simulation(10))
    sim2 = Simulation(0, 10, 5)
    print(sim2.run_simulation(10))




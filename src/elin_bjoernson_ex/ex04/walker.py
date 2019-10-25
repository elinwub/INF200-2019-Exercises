# -*- coding: utf-8 -*-
import random

__author__ = 'Elin Bjørnson'
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
        if self.position == self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.position

    def get_steps(self):
        return self.moves


def walk(dist, pos, h):
    for i in range(len(dist)):
        moves = []
        for j in range(5):
            walker = Walker(pos[i], h[i])
            while walker.is_at_home() == False:
                walker.move()

            moves.append(walker.get_steps())
        return print(f'Distance: {dist[i]} -> Path lengths: {moves}')


if __name__ == '__main__':
    distances = [1, 2, 5, 10, 20, 50]
    initial_positions = [random.randint(0, 100) for i in range(len(distances))]
    home = [(x+y) for x, y in zip(distances, initial_positions)]
    print(walk(distances, initial_positions, home))




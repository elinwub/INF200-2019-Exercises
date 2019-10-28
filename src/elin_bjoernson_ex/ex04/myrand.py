# -*- coding: utf-8 -*-
import random

__author__ = 'Elin Bjørnson'
__email__ = 'elinbj@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.seed = seed

    def rand(self):
        """ Returns the next random number"""
        a = 7**5
        m = 2**31-1
        next_num = (a * self.seed) % m
        self.seed = next_num
        return next_num


class ListRand:
    def __init__(self, random_list):
        self.random_list = random_list
        self.times = 0

    def rand(self):
        """ Returns the next random number"""
        if len(self.random_list) == self.times:
            raise RuntimeError
        next_num = self.random_list[self.times]
        self.times += 1
        return next_num


if __name__ == '__main__':
    rand_num = LCGRand(random.randint(0, 10))
    print(rand_num.rand())
    print(rand_num.rand())

    list_rand = ListRand([random.randint(0, 10) for i in range(3)])
    print(list_rand.rand())
    print(list_rand.rand())
    print(list_rand.rand())
    print(list_rand.rand())

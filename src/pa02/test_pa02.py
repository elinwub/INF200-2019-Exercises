# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Elin Wølner Bjørnson'
__email__ = 'jaer@nmbu.no', 'elinbj@nmbu.no'

import chutes_simulation as cs
import random
import pytest


class TestBoard:

    def test_only_one_input(self):
        """Tests if we get get standard board, if we only have one input"""
        b_std = cs.Board()
        b = cs.Board([(1, 4), (5, 16)])
        assert b.board == b_std.board



    def test_only_goal_input(self):
        """Tests if we get get standard board and goal, if we only have one
        input"""
        b_std = cs.Board()
        b = cs.Board(goal = 89)
        assert b.board == b_std.board



    def test_standard_goal_is_90(self):
        b = cs.Board()
        assert b.goal == 90


    def test_goal_is_same_as_given(self):
        goal = 30
        b = cs.Board(ladders=[(1, 4)], chutes=[(9, 2)], goal = goal)
        assert b.goal == goal


    def test_std_goal_is_not_same_as_30(self):
        goal = 30
        b = cs.Board(goal = goal)
        assert b.goal != goal






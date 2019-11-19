# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Elin Wølner Bjørnson'
__email__ = 'jaer@nmbu.no', 'elinbj@nmbu.no'

import chutes_simulation as cs
import random
import pytest


class TestBoard:

    def test_only_one_input(self):
        """
        Tests if we get get standard board if we only have one input
        """
        b_std = cs.Board()
        b = cs.Board([(1, 4), (5, 16)])
        assert b.board == b_std.board

    def test_only_goal_input(self):
        """
        Tests if we get get standard board and goal, if we only have one
        input
        """
        b_std = cs.Board()
        b = cs.Board(goal=89)
        assert b.board == b_std.board

    def test_standard_goal_is_90(self):
        """
        Tests that standard goal position is 90
        """
        b = cs.Board()
        assert b.goal == 90

    def test_goal_is_same_as_given(self):
        """
        Tests that goal position is the same as the given input goal.

        """
        goal = 30
        b = cs.Board(ladders=[(1, 4)], chutes=[(9, 2)], goal=goal)
        assert b.goal == goal

    def test_std_goal_is_not_same_as_30(self):
        """
        Tests that standard goal is not 30

        """
        goal = 30
        b = cs.Board(goal=goal)
        assert b.goal != goal

    def test_position_adjustment_returns_0_on_regular_spot(self):
        """
        Tests that position_adjustment returns 0 when player doesn't land on a
        chute or ladder
        """
        b = cs.Board()
        position = 2
        zero = b.position_adjustment(position)
        assert zero == 0


class TestPlayerTypes:
    def test_player_position_changes(self):
        """
        Tests that player position changes after a move
        """
        p = cs.Player()
        p.move()
        assert p.position != 0

    def test_uses_standard_board_if_not_added(self):
        """
        Tests that ResilientPlayer can move if a board is not added
        """
        r = cs.ResilientPlayer()
        r.move()

    def test_uses_standard_board_if_not_added(self):
        """
        Tests that LazyPlayer can move if a board is not added
        """
        l = cs.LazyPlayer()
        l.move()



class TestSimulation:

    def test_same_winner_single_game_with_given_seed(self):
        """
        Test if the seed works, giving the same winners
        """
        players = [cs.Player, cs.LazyPlayer]
        sim = cs.Simulation(player_field=players, seed=1)
        winner = sim.single_game()
        sim2 = cs.Simulation(player_field=players, seed=1)
        test_winner = sim2.single_game()

        assert winner == test_winner



    def test_known_winner_in_single_game_with_given_seed(self):
        """
        Tests if the winner is same as a given winner, with given seed
        """
        players = [cs.Player, cs.LazyPlayer]
        sim = cs.Simulation(player_field=players, seed=1)
        winner = sim.single_game()
        test_winner = (29, 'Player')

        assert winner == test_winner




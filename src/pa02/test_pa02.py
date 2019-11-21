# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Elin Wølner Bjørnson'
__email__ = 'jaer@nmbu.no', 'elinbj@nmbu.no'

import chutes_simulation as cs
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

    def test_uses_standard_board_if_not_added_resilient(self):
        """
        Tests that ResilientPlayer can move if a board is not added
        """
        r = cs.ResilientPlayer()
        r.move()
        assert r.position != 0


    def test_uses_standard_board_if_not_added_lazy(self):
        """
        Tests that LazyPlayer can move if a board is not added
        """
        lp = cs.LazyPlayer()
        lp.move()
        assert lp.position != 0


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


    def test_randomize_players(self):
        """
        Tests if the shuffle works, and gives different result with same seed
        """
        p = [cs.Player, cs.Player, cs.ResilientPlayer, cs.ResilientPlayer,
                          cs.ResilientPlayer, cs.LazyPlayer]
        sim1 = cs.Simulation(p, randomize_players=True)
        sim2 = cs.Simulation(p, randomize_players=False)

        sim1.run_simulation(10)
        sim2.run_simulation(10)

        assert sim1.get_results() is not sim2.get_results()


    def test_players_per_type_is_zero(self):
        """
        Tests if no players, gives a dictionary without players in the counter
        """

        player_types = {'Player': 0, 'LazyPlayer': 0, 'ResilientPlayer': 0}
        p = []
        sim = cs.Simulation(p)

        assert sim.players_per_type() == player_types


    def test_players_per_type_is_one(self):
        """
        Tests if we have one of each players
        """

        player_types = {'Player': 1, 'LazyPlayer': 1, 'ResilientPlayer': 1}
        p = [cs.Player, cs.LazyPlayer, cs.ResilientPlayer]
        sim = cs.Simulation(p)

        assert sim.players_per_type() == player_types






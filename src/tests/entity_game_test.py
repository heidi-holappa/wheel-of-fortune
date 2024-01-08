from unittest import TestCase

from entities.game import Game


class TestEntityPlayer(TestCase):

    def setUp(self):
        pass

    def test_a_new_game_starts_at_turn_zero(self):
        game = Game()
        self.assertEqual(game.turn, 0)

    def test_turn_can_be_incremented(self):
        game = Game()
        game.increment_turn()
        self.assertEqual(game.turn, 1)

    def test_turn_can_be_incremented_multiple_times(self):
        game = Game()
        game.increment_turn()
        game.increment_turn()
        self.assertEqual(game.turn, 2)

    def test_a_player_can_be_added_to_the_game(self):
        game = Game()
        game.add_player("John Doe")
        self.assertEqual(len(game.players), 1)

    def test_game_returns_the_player_whose_turn_it_is(self):
        game = Game()
        game.add_player("John Doe")
        game.add_player("Jane Doe")
        self.assertEqual(game.current_player().name, "John Doe")

    def test_game_returns_the_player_whose_turn_it_is_after_increment(self):
        game = Game()
        game.add_player("John Doe")
        game.add_player("Jane Doe")
        game.increment_turn()
        self.assertEqual(game.current_player().name, "Jane Doe")

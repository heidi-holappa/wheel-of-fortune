from unittest import TestCase

from entities.player import Player


class TestEntityPlayer(TestCase):

    def setUp(self):
        pass

    def test_a_new_player_can_be_created(self):
        player = Player("John Doe")
        self.assertEqual(player.name, "John Doe")

    def test_a_new_player_has_a_balance_of_zero(self):
        player = Player("John Doe")
        self.assertEqual(player.balance, 0)

    def test_balance_increment_is_stored_to_player(self):
        player = Player("John Doe")
        player.increment_balance(100)
        self.assertEqual(player.balance, 100)

    def test_resetting_balance_set_balance_to_zero(self):
        player = Player("John Doe")
        player.increment_balance(100)
        player.reset_balance()
        self.assertEqual(player.balance, 0)

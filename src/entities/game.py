from entities.player import Player


class Game:

    def __init__(self):
        self.turn = 0
        self.players = []

    def increment_turn(self):
        self.turn += 1

    def add_player(self, name):
        self.players.append(Player(name))

    def current_player(self) -> Player:
        return self.players[self.turn % len(self.players)]

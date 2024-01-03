from entities.player import Player
import os


def generate_players(n_players: int):
    players = []

    for i in range(n_players):
        name = input(f"Player {i + 1} name: ")
        players.append(Player(name))
    os.system('clear')
    return players

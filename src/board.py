from player import Player
from wheelAnimation import WheelAnimation
import math


class Board:

    def __init__(self):
        self.width = 40
        self.wheel = WheelAnimation()

    def render_header(self, player: Player):
        print("_" * self.width)
        self.render_empy_line()
        player_name = "PLAYER: " + player.name
        balance = "BALANCE: " + str(player.balance)
        l_marginal = "|  "
        r_marginal = "  |"
        empty_spaces = self.width - \
            len(player_name) - len(balance) - len(l_marginal) - len(r_marginal)
        print(l_marginal + player_name + " " *
              empty_spaces + balance + r_marginal)
        self.render_empy_line()

    def render_wheel_to_board(self):
        wheel_render, prize_information = self.wheel.render_wheel(4)
        wheel_height = len(self.wheel.wheel)
        wheel_width = len(self.wheel.wheel[0])
        l_margin = "|  "
        r_margin = "  |"
        reserved_width = len(l_margin) + len(r_margin) + wheel_width
        empty_space_left = math.floor((self.width - reserved_width) / 2)
        empty_space_right = math.ceil((self.width - reserved_width) / 2)
        self.render_empy_line()
        for i in range(wheel_height):
            print(l_margin + " " * empty_space_left +
                  wheel_render[i] + " " * empty_space_right + r_margin)

    def render_footer(self, prize_info: str):
        self.render_empy_line()
        l_margin = "|  "
        r_margin = "  |"
        empty_space_left = math.floor(
            (self.width - len(prize_info) - len(l_margin) - len(r_margin)) / 2)
        empty_space_right = math.ceil(
            (self.width - len(prize_info) - len(l_margin) - len(r_margin)) / 2)
        print(l_margin + " " * empty_space_left +
              prize_info + " " * empty_space_right + r_margin)
        self.render_empy_line()
        print("|" + "_" * (self.width - 2) + "|")

    def render_empy_line(self):
        print("|" + " " * (self.width - 2) + "|")


if __name__ == "__main__":
    player = Player("Test")
    player.balance = 1000
    board = Board()
    board.render_header(player)
    board.render_wheel_to_board()
    board.render_footer("Bandit. Lost everything")

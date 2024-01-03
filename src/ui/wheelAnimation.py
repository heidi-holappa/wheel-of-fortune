import os
import random
import time

from enum import Enum


class Prizes(Enum):
    BANDIT = 1
    MISSTURN = 2
    MONEY = 3


class WheelAnimation:

    def __init__(self):
        self.wheel = [
            [' ', ' ', ' ', '=', ' ', '=', ' ', ' ', ' '],
            [' ', '=', ' ', ' ', ' ', ' ', ' ', '=', ' '],
            ['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
            [' ', '=', '=', ' ', '=', ' ', '=', '=', ' '],
            ['=', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '='],
            [' ', '=', ' ', ' ', ' ', ' ', ' ', '=', ' '],
            [' ', ' ', ' ', '=', ' ', '=', ' ', ' ', ' ']
        ]
        self.rotation = False
        self.start_pos = random.randint(0, 12)
        self.prizes = [
            (Prizes.MONEY, 100),
            (Prizes.MISSTURN, 0),
            (Prizes.MONEY, 300),
            (Prizes.MONEY, 500),
            (Prizes.MISSTURN, 0),
            (Prizes.MONEY, 1000),
            (Prizes.BANDIT, 0),
            (Prizes.MONEY, 500),
            (Prizes.MONEY, 100),
            (Prizes.MONEY, 300),
            (Prizes.MONEY, 100),
            (Prizes.MONEY, 300),
        ]

    def spin_wheel(self):
        rounds = random.randint(12, 24)
        pos = 0
        for i in range(rounds):
            os.system('clear')
            pos = (self.start_pos + i) % 11
            self.render_wheel(pos)
            self.rotation = bool(not self.rotation == True)
            time.sleep(0.15 + i / 100)
        self.start_pos = pos
        return self.prizes[pos]

    def render_wheel(self, pos):
        output_list = []
        print_pos = [(0, 4), (1, 6), (2, 7), (4, 8), (6, 7), (7, 6),
                     (8, 4), (7, 2), (6, 1), (4, 0), (2, 1), (1, 2)]
        for i in range(len(self.wheel)):
            output = ""
            for j in range(len(self.wheel[0])):
                if (i, j) == print_pos[pos]:
                    output += "o"
                    continue
                if not self.rotation:
                    output += self.wheel[i][j]
                else:
                    output += self.wheel[j][i]
            output_list.append(output)
        return output_list, self.prizes

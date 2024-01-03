import os
import time
import random
from ui.wheelAnimation import WheelAnimation, Prizes
from entities.player import Player

with open("dict.txt", "r", encoding="utf-8") as f:
    entries = f.read().split('\n')

players = []

while (True):
    try:
        players_num = int(input("How many players? "))
        for i in range(players_num):
            name = input(f"Player {i + 1} name: ")
            players.append(Player(name))
        os.system('clear')
        break
    except ValueError:
        print("Please enter a number.")

default_show = {"!", ".", "'", "?", ",", "-", ":", " "}

author, entry = random.choice(entries).split(':', 1)
entry = entry.strip()
wheel = WheelAnimation()

guesses = set()

wheel_spun = False
turn_over = False
balance = 0
money_offer = 0
turn = 0
turn_used = False

while (True):
    current_player = players[turn % len(players)]
    print(f"{current_player.name}'s turn")
    output = ""
    for c in entry:
        if c.lower() not in guesses and c not in default_show:
            output += "_"
        else:
            output += c
    print(f"OUTPUT: {output}")
    print("ACTION:")
    print("1. Guess a letter")
    print("2. Guess the phrase")
    print("3. Spin the wheel")
    try:
        user_choice = int(input("Choice: "))
    except ValueError:
        print("Please enter a number.")
        continue
    if user_choice == 1:
        if not wheel_spun:
            print("You need to spin the wheel first.")
            continue
        char = input("Letter: ").lower()
        if char not in guesses and char in entry.lower():
            guesses.add(char)
            print("Correct!")
            current_player.increase_balance(money_offer)
            turn_used = False
        else:
            print("Incorrect!")
            time.sleep(1)
            os.system('clear')
            turn_used = True
            turn += 1
        wheel_Spun = False
        money_offer = 0

    if user_choice == 2:
        if not wheel_spun or turn_used:
            print("You need to spin the wheel first.")
            continue
        guess = input("Your guess: ")
        if guess.lower().split() == entry.lower().split():
            print("Correct!")
            print(f"Congratulations {current_player.name}!")
            print(f"The answer was '{entry}'( - {author})")
            current_player.increase_balance(money_offer)
            break
        print("Incorrect!")
        wheel_spun = False
        turn_used = True
        turn += 1
        money_offer = 0
        time.sleep(1)
    if user_choice == 3:
        if wheel_spun:
            print("You already spun the wheel.")
            continue
        enum_value, int_value = wheel.spin_wheel()
        match enum_value:
            case Prizes.BANDIT:
                current_player.reset_balance()
                turn_used = True
                turn += 1
                wheel_spun = True
                money_offer = 0
            case Prizes.MISSTURN:
                turn_used = True
                turn += 1
                wheel_spun = True
                money_offer = 0
            case Prizes.MONEY:
                money_offer = int_value
                wheel_spun = True
                turn_used = False
            case _:
                continue

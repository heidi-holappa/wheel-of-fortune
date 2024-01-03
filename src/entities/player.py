class Player:
    def __init__(self, name: str):
        self.name = name
        self.balance = 0

    def reset_balance(self):
        self.balance = 0

    def increment_balance(self, amount: int):
        self.balance += amount

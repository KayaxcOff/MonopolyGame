import json
import random

class MonopolyGame:
    @staticmethod
    def read_json(file_name):
        with open(file_name, 'r') as f:
            monopoly_data = json.load(f)
        return monopoly_data

    def __init__(self, player_data):
        self.field = [None] * 40
        self.player = Player(player_data)

    @staticmethod
    def roll_dice():
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        return die_1 + die_2

    def pay_rent(self):
        self.rent_light = 10
        self.rent_normal = 25
        self.rent_heavy = 50

class Player:
    def __init__(self, data):
        self.name = data['name']
        self.money = data['cash']
        self.debt = data['debt']
        self.position = data['position']

    def move(self, steps, board_size=40):
        self.position = (self.position + steps) % board_size

    def properties(self):
        self.mediterranean_avenue
        self.boardwalk

data = MonopolyGame.read_json('monoGame.json')
player_data = data['players'][0]
game = MonopolyGame(player_data)

dice = MonopolyGame.roll_dice()
game.player.move(dice)

print(f"{game.player.name} new position: {game.player.position}")

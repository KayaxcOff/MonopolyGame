import json
import random

file_path = "monoGame.json"

class MonopolyGame:
    def __init__(self):
        pass

    def players(self):
        with open(file_path) as json_file:
            self.players_data = json.load(json_file)
        self.name = self.players_data[0]["name"]
        self.cash = self.players_data[0]["cash"]
        self.debt = self.players_data[0]["debt"]
        self.properties = self.players_data[0]["properties"]
        self.position = self.players_data[0]["position"]

    def roll_dice(self):
        self.dice_1 = random.randint(1, 6)
        self.dice_2 = random.randint(1, 6)
        self.total_roll = self.dice_1 + self.dice_2
        return self.total_roll

    def gameField(self):
        self.matris = [None] * 40
        self.matris[random.randint(0, 39)] = {"type" : "house", "name" : "UltraTech"}
        self.matris[random.randint(0, 39)] = {"type" : "house", "name" : "Bank"}
        self.matris[random.randint(0, 39)] = {"type" : "house", "name" : "Google House"}
        self.matris[random.randint(0, 39)] = {"type" : "house", "name" : "Prison"}
        self.matris[random.randint(0, 39)] = {"type" : "house", "name" : "Home of the Future"}
        return self.matris

class MonopolyGamePlayer:
    def __init__(self):
        pass

    def player_info(self):
        self.players()

    def player_position(self):
        pass

    def pay_rent(self):
        self.mono = MonopolyGame()
        self.rentForProperty = {
            "UltraTech": 100,
            "Bank": 150,
            "Google House": 200,
            "Prison": 250,
            "Home of the Future": 300
        }

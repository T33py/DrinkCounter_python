import string
from drink import Drink
from datetime import datetime

class Person:

    def __init__(self, name:str):
        self.name = name
        self.drunk:list[(Drink, datetime)] = []

    def drink(self, drink:Drink):
        self.drunk.append((drink, datetime.now()))
        print(f'{self.name} drank {drink.name}')

    def individual_drinks(self):
        drink_counts:dict[Drink, int] = {}

        for drunken in self.drunk:
            drink = drunken[0]
            if drink in drink_counts.keys():
                drink_counts[drink] += 1
            else:
                drink_counts[drink] = 1

        return drink_counts
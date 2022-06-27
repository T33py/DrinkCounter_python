from drink import Drink
from person import Person


class Data:
    drinks:list[Drink] = []
    people:list[Person] = []

    def add_drink(self, drink:Drink):
        self.drinks.append(drink)

    def add_person(self, person:Person):
        self.people.append(person)

    def person_drinks_drink(self, person:Person, drink:Drink):
        person.drink(drink)
        print(f'{person.name} drank {drink.name}')

    def remove_drink(self, drink:Drink):
        self.drinks.remove(drink)
    
    def remove_person(self, person:Person):
        self.people.remove(person)

    def person_didnt_drink_drink(self, person:Person, drink:Drink):
        person.drunk.remove(drink)

    def export(self):
        titles = 'person;beverage;percetage;size;time\n'
        rows = [titles]
        for person in self.people:
            for (drink, time) in person.drunk:
                row = f'{person.name};{drink.name};{str(drink.percentage).replace(".", ",")};{drink.size};{str(time).replace(".", ",")}\n'
                rows.append(row)
        
        f = open('export.csv', 'w')
        f.writelines(rows)
        f.close()
        
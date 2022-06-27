import imp
import tkinter as tk
from tkinter import ttk

from data import Data
from drink import Drink
from person import Person

class GUI:

    displayed_drinks:list[Drink] = []
    drinks_frames:dict[Drink, tk.Frame] = {}
    drinks_labels:dict[Drink, tk.Label] = {}
    drinks_drink_buttons:dict[Drink, tk.Button]= {}
    drinks_delete_buttons:dict[Drink, tk.Button]= {}
    drinks_sepperators:dict[Drink, ttk.Separator] = {}
    longest_drink_display_text:int = 0

    displayed_people:list[Person] = []
    selected_people:list[Person] = []
    people_frames:dict[Person, tk.Frame] = {}
    people_drunk_frames:dict[Person, tk.Frame] = {}
    people_labels:dict[Person, tk.Label] = {}
    people_drunk_displays:dict[Person, list[tk.Label]] = {}
    people_choose_buttons:dict[Person, tk.Button] = {}
    people_delete_button:dict[Person, tk.Button] = {}


    def __init__(self):
        self.data = Data()
        self.window = tk.Tk()
        self.create_drinks_display()
        self.create_people_display()

        if len(self.data.drinks) == 0:
            self.data.add_drink(Drink('pils', 4.5, 33))
            self.data.add_drink(Drink('snaps', 40, 2))
            self.data.add_drink(Drink('cola', 0, 50))
            self.data.add_person(Person('jones'))
            self.data.add_person(Person('jules'))
            self.data.add_person(Person('tb'))
            self.data.add_person(Person('Razz'))
            self.longest_drink_display_text = 5


    def create(self):
        header_frame = tk.Frame(
            master=self.window,
            borderwidth=2
        )
        drinks_frame = tk.Frame(
            master=self.window,
            borderwidth=2
        )
        drink_name_frame = tk.Frame(
            master=drinks_frame,
            borderwidth=2
        )
        alc_frame = tk.Frame(
            master=drinks_frame,
            borderwidth=2
        )
        size_frame = tk.Frame(
            master=drinks_frame,
            borderwidth=2
        )
        add_drink_button_frame = tk.Frame(
            master=drinks_frame,
            borderwidth=2
        )
        persons_frame = tk.Frame(
            master=self.window,
            borderwidth=2
        )
        person_name_frame = tk.Frame(
            master=persons_frame,
            borderwidth=2
        )
        add_person_button_frame = tk.Frame(
            master=persons_frame,
            borderwidth=2
        )
        

        drinks_frame.grid(row=1, column=0)
        persons_frame.grid(row=1, column=1)

        drink_name_frame.grid(row=0, column=0)
        alc_frame.grid(row=0, column=1)
        size_frame.grid(row=0, column=2)
        add_drink_button_frame.grid(row=0, column=3)
        self.drinks_display_frame.grid(row=2, column=0)

        person_name_frame.grid(row=0, column=0)
        add_person_button_frame.grid(row=0, column=1)




        greeting = tk.Label(text='Hello World!', master=header_frame)
        header_frame.grid(row=0, column=0)
        greeting.pack()

        drink_name = self.spawn_input_field('Name', drink_name_frame)
        person_name = self.spawn_input_field('Name', person_name_frame)
        
        drink_percentage = self.spawn_input_field('Alkohol %', alc_frame)
        
        drink_size = self.spawn_input_field('Size (cl)', size_frame)
        
        btn_add_drink = tk.Button(
            master=add_drink_button_frame,
            text='Add drink',
            height=1,
            width=10,
            bg='grey',
            command=self.add_drink(drink_name[1].get, drink_percentage[1].get, drink_size[1].get)
        )
        btn_add_drink.pack(side=tk.BOTTOM)

        btn_add_person = tk.Button(
            master=add_person_button_frame,
            text='Add person',
            height=1,
            width=10,
            bg='grey',
            command=self.add_person(person_name[1].get)
        )
        btn_add_person.pack()

        btn_export = tk.Button(
            master=header_frame,
            text='Export',
            height=1,
            width=10,
            bg='grey',
            command=self.data.export
        )
        btn_export.pack(side=tk.LEFT)

        self.update()
        return self.window


    def update_label(self, label, text_getter):
        def exec():
            print(text_getter())
            label['text'] = text_getter()
        return exec

    def spawn_input_field(self, name, frame):
        lbl = tk.Label(master=frame, text=name)
        ent = tk.Entry(master=frame)
        lbl.pack()
        ent.pack()
        return (lbl, ent)

    def add_drink(self, name, alc, size):
        def exec():
            n = name()
            a = alc().replace(',', '.')
            s = size()
            print(f'Creating drink {n}: {a}%, {s}cl')
            drink = Drink(n, float(a), int(s))
            self.data.add_drink(drink)
            if len(n) > self.longest_drink_display_text:
                self.longest_drink_display_text = len(n)
            self.update()
        return exec

    def add_person(self, name):
        def exec():
            n = name()
            print(f'Creating person {n}')
            person = Person(n)
            self.data.add_person(person)
            self.update()
        return exec

    def create_drinks_display(self):        
        self.drinks_display_frame = tk.Frame(
            master=self.window,
            borderwidth=4
        )
        self.drinks_display_frame.grid(row=2, column=0)

    
    def create_people_display(self):        
        self.people_display_frame = tk.Frame(
            master=self.window,
            borderwidth=4
        )
        self.people_display_frame.grid(row=2, column=1)
        
    def drink_text(self, drink:Drink):
        return f'{drink.name}: {drink.percentage}% , {drink.size} cl'

    def update_drinks_display(self):
        rw = 0
        for drink in self.data.drinks:
            default_text = self.drink_text(drink)
            if len(default_text) > self.longest_drink_display_text:
                self.longest_drink_display_text = len(default_text)
            
            # if its a new drink
            if drink not in self.displayed_drinks:
                drink_frame = tk.Frame(
                    master=self.drinks_display_frame,
                    borderwidth=2
                )
                lbl = tk.Label(
                    master= drink_frame,
                    text = default_text,
                    padx= 10 + (self.longest_drink_display_text - len(default_text))
                )
                drink_btn = tk.Button(
                    master=drink_frame,
                    text='Drink',
                    bg='green',
                    command=self.person_drinks_drink(drink)
                )
                delete_btn = tk.Button(
                    master=drink_frame,
                    text='Delete',
                    bg='red',
                    command=self.remove_drink(drink)
                )
                sep = ttk.Separator(orient='horizontal', master=self.drinks_display_frame)

                drink_frame.pack()
                sep.pack(fill='x')
                lbl.grid(
                    row=rw, 
                    column=0,
                    sticky='w'
                )
                drink_btn.grid(row=rw, column=3)
                delete_btn.grid(row=rw, column=4)
                

                #register elements for later use
                self.drinks_frames[drink] = drink_frame
                self.drinks_labels[drink] = lbl
                self.drinks_drink_buttons[drink] = drink_btn
                self.drinks_delete_buttons[drink] = delete_btn
                self.drinks_sepperators[drink] = sep
                self.displayed_drinks.append(drink)

                rw +=1
            
            

        
    def update_people_display(self):
        # print('update ppl')
        for person in self.data.people:
            # print(f'display {person.name}')
            drunk_labels = self.format_drunk_displaytext(person)

            # if its a new person
            if person not in self.displayed_people:
                person_frame = tk.Frame(
                    master=self.people_display_frame,
                    borderwidth=2
                )
                drunk_frame = tk.Frame(
                    master=person_frame,
                    borderwidth=2
                )
                name_lbl = tk.Label(
                    master= person_frame,
                    text = person.name,
                    padx= 10
                )
                select_btn = tk.Button(
                    master=person_frame,
                    text='Choose for drink',
                    bg='grey',
                    command=self.select_person(person)
                )
                delete_btn = tk.Button(
                    master=person_frame,
                    text='Delete',
                    bg='red',
                    command=self.remove_person(person)
                )
                
                person_frame.pack()
                name_lbl.grid(row=0, column=0, sticky='w')
                drunk_frame.grid(row=1, column=0)
                select_btn.grid(row=2, column=0)
                delete_btn.grid(row=2, column=1)
                
                drunk_labels = []
                rw = 0
                for text in drunk_labels:
                    # print(f'label: {text}')
                    label = tk.Label(text=text, master=drunk_frame)
                    drunk_labels.append(label)
                    label.grid(row=rw, column=0)

                #register elements for later use
                self.people_frames[person] = person_frame
                self.people_drunk_frames[person] = drunk_frame
                self.people_labels[person] = name_lbl
                self.people_drunk_displays[person] = drunk_labels
                self.people_choose_buttons[person] = select_btn
                self.people_delete_button[person] = delete_btn
                self.displayed_people.append(person)

            else:
                if len(self.people_drunk_displays[person]) < len(drunk_labels):
                    for i in range(len(drunk_labels) - len(self.people_drunk_displays[person])):
                        # print(f'new label')
                        label = tk.Label(master=self.people_drunk_frames[person])
                        self.people_drunk_displays[person].append(label)
                        label.grid(row=len(self.people_drunk_displays[person]), column=0)

                for idx in range(len(self.people_drunk_displays[person])):
                    # print(f'label: {drunk_labels[idx]}')
                    self.people_drunk_displays[person][idx]['text'] = drunk_labels[idx]


        


    def format_drunk_displaytext(self, person:Person):
        labels:list[str] = []
        drinks = person.individual_drinks()
        for drink in drinks.keys():
            text = ''
            text = f'{text}{drink.name}: {drink.percentage}%  |  Consumed: {drinks[drink]}'
            # print(text)
            labels.append(text)
        return labels

    def person_drinks_drink(self, drink:Drink):
        def exec():
            for person in self.selected_people:
                person.drink(drink)
            self.update()
        return exec

    def select_person(self, person:Person):
        def exec():
            if person in self.selected_people:
                self.people_choose_buttons[person]['bg'] = 'grey'
                self.selected_people.remove(person)
            else:
                self.people_choose_buttons[person]['bg'] = 'green'
                self.selected_people.append(person)
        return exec

    def remove_person(self, person:Person):
        def exec():
            print(f'remove {person.name}')
            self.people_frames[person].destroy()
            self.displayed_people.remove(person)
            self.data.remove_person(person)
            self.update()
        return exec

    def remove_drink(self, drink:Drink):
        def exec():
            self.drinks_frames[drink].destroy()
            self.drinks_sepperators[drink].destroy()
            self.displayed_drinks.remove(drink)
            self.data.remove_drink(drink)
            self.update()
        return exec

    def update(self):
        # print('update')
        self.update_drinks_display()
        self.update_people_display()
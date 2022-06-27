import tkinter as tk

from data import Data
from drink import Drink
from window import GUI

buttons = 1

def main():
    print('init')
    data = Data()
    builder = GUI()
    print('Create window')
    wnd = builder.create()
    wnd.mainloop()
    print('Closed app')

if __name__ == '__main__':
    main()
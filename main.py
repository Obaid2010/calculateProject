import math
from tkinter import *

screen = Tk()
screen.title("Calculator")
screen.minsize(width=350, height=450)
screen.config(padx=10, pady=10)

display = Entry(screen, width=15, font=("Arial", 24),)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, END)

def button_equal():
    expression = display.get()
    try:
        result = eval(expression)
        display.delete(0, END)
        display.insert(0, result)
    except:
        display.delete(0, END)
        display.insert(0, "Error")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
]

for (text, row, col) in buttons:
    button = Button(screen, text=text, width=5, height=2, font=("Arial", 16))
    button.grid(row=row, column=col, padx=5, pady=5)
    button.config(command=lambda t=text: button_click(t))

equal_button = Button(screen, text='=', width=5, height=2, font=("Arial", 16), command=button_equal)
equal_button.grid(row=4, column=3, padx=5, pady=5)

clear_button = Button(screen, text="C", width=5, height=2, font=("Arial", 16), command=button_clear)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

screen.mainloop()

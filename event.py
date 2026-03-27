from tkinter import *

window = Tk()

def select(arg):
    selection = "I'll have the " + sandwich_var.get() + " sandwich with " + juice_var.get() + " juice"
    label.config(text=selection)

sandwich_var = StringVar()
sandwich_var.set("ham")
juice_var = StringVar()
juice_var.set("orange")

dropdown_1 = OptionMenu(window, sandwich_var, "ham", "cheese", "chicken", command=select)
dropdown_1.pack()

dropdown_2 = OptionMenu(window, juice_var, "orange", "apple", "kiwi", command=select)
dropdown_2.pack()

label = Label(window)
label.pack()

window.mainloop()


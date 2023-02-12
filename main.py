from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Combobox example")
root.geometry("250x200")


def selected(event):
    selection = combobox.get()
    print(selection)


country = ["Russia", "France", "China", "Spain"]
combobox = ttk.Combobox(values=country, state="readonly")
combobox.pack()
combobox.bind("<<ComboboxSelected>>", selected)
print("Programm started")
root.mainloop()
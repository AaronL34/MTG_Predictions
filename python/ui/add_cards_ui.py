import tkinter as tk
from back_end.add_card import add_card

def add_new_card_ui():
    top = tk.Toplevel()
    top.title("Add a New Card")
    top.geometry("300x500")
    tk.Label(top, text="Color").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(top, text="Type").grid(row=0, column=2, padx=5, pady=5)
    tk.Label(top, text="Description").grid(row=1, column=0, padx=5, pady=5)
    tk.Text(top, height=6, width=10).grid(row=2, column=0, padx=5, pady=5)

    Colors = [
    "White",
    "Black",
    "Blue",
    "Red",
    "Green"
    ]
    Types = [
    "Land",
    "Instant",
    "Sorcery",
    "Creature",
    "Planswalker",
    "Battle"
    ]
    first_color = tk.StringVar(top)
    first_color.set(Colors[0])
    first_type = tk.StringVar(top)
    first_type.set(Types[0])

    tk.OptionMenu(top, first_color, *Colors).grid(row=0, column=1, padx=5, pady=5)
    tk.OptionMenu(top, first_type, *Types).grid(row=0, column=3, padx=5, pady=5)


    tk.Button(top, text="Close", command=top.destroy).grid(row=4, column=0, padx=5, pady=5)
    tk.Button(top, text="Add Card", command=add_card).grid(row=4, column=1, padx=5, pady=5)
    top.mainloop()

import tkinter as tk
from back_end.add_card import add_card

def add_new_card_ui():
    top = tk.Toplevel()
    top.title("Add a New Card")
    top.geometry("300x500")
    tk.Button(top, text="close", command=top.destroy).grid(row=0, column=0, padx=5, pady=5)

    tk.Button(top, text="Add Card", command=add_card).grid(row=1, column=0, padx=5, pady=5)
    top.mainloop()

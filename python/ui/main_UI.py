import tkinter as tk
import ui.add_cards_ui as acui
import os


def main_ui():
    root = tk.Tk()
    root.title("MTG Predictions")
    root.geometry("700x500")
    tk.Button(root, text="Add a New Card", command=acui.add_new_card_ui).pack()


    root.mainloop()




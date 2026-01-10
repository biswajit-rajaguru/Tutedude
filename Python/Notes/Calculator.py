# main.py

import tkinter as tk
from CalculatorUI import CalculatorUI
from CalculatorLogic import CalculatorLogic


def Calculator():
    root = tk.Tk()
    root.geometry("700x500")
    root.title("Calculator")

    logic = CalculatorLogic()

    def handle_key(key):
        key_map = {"×": "*", "÷": "/"}
        value = logic.process_input(key_map.get(key, key))
        ui.set_display(value)

    ui = CalculatorUI(root, on_key=handle_key)
    root.mainloop()


if __name__ == "__main__":
    Calculator()
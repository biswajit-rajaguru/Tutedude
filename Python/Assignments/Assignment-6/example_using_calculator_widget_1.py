import tkinter as tk
from CalculatorWidget import Calculator

root = tk.Tk()
root.geometry("700x500")
root.title("Calculator")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)

calculator = Calculator(root)
calculator.grid(row = 0, column = 0, sticky = "nsew")

root.mainloop()

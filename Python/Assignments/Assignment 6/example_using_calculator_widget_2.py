import tkinter as tk
from CalculatorWidget import Calculator

theme_file_names = [
    "basic_calculator_theme_file.json",
    "cyberpunk_calculator_theme_file.json",
    "retropop_calculator_theme_file.json",
    "midnight_calculator_theme_file.json"]

root = tk.Tk()
root.geometry("700x500")
root.title("Multiple Calculators")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.columnconfigure(1, weight = 1)

#this is just an array to store references to the calculators 
calculators = [1,2,3,4]
for i in range(4):
    calculators[i] = Calculator(root,theme_file_names[i])
    calculators[i].grid(row = i//2, column = i%2, sticky = "nsew")

root.mainloop()


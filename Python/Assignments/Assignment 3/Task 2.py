"""

Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
    1.   Asks the user for a number as input.
    2.   Uses the math module to calculate the:
         o   Square root of the number
         o   Natural logarithm (log base e) of the number
         o   Sine of the number (in radians)
    3.   Displays the calculated results.

"""


import math  # import the math module 

x = float(input("Enter a number: ")) # cast the input to a float

# Use the sqrt function in math module
print(f"Square root: {math.sqrt(x)}") 

# The log function in math module calculates the natural logarithm 
print(f"Logarithm: {math.log(x)}")

# The sin function in math module calculates the sine of x, when x is in radians.
print(f"Sine: {math.sin(x)}")



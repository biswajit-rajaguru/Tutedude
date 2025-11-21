"""

Task 1: Check if a Number is Even or Odd

Problem Statement:  Write a Python program that:
    1. 	Takes an integer input from the user.
    2. 	Checks whether the number is even or odd using an if-else statement.
    3. 	Displays the result accordingly.

"""
# ask the user to enter a number and cast the input to int to input an integer from the user 
num = int(input("Enter a number: ")) 

# A one-line if-else statement/expression has the form:
# (true expression) if (conditional expression) else (false expression)
# The  true and false expressions can be used to execute statements conditionally. This is the form we have used.
# the conditional expression evaluates to true when num % 2 is 0 . Then the true expression prints that the number is even
# if the conditional expression evaluates to false then the false expression prints that the number is odd

print(f"{num} is an even number.") if num % 2 == 0 else print(f"{num} is an odd number.")

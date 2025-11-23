# Task 1

## Task 1: Calculate Factorial Using a Function

### Problem Statement: Write a Python program that

    1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
    2.   Returns the calculated factorial.
    3.   Calls the function with a sample number and prints the output.

## Solution

- I define a function named factorial which takes a single argument. It returns "Error" if the argument is not a nonnegative integer but if the argument is a nonnegative integer, then it returns the factorial of the argument.
- I have a docstring explaining the input and output of the function.
- Then I check that the argument is a nonnegative integer. If it is not, then I return "Error".
- I use the variable named factorial to accumulate the product of the factors n, n-1,...,1.
- I initialize the vatiable factorial to 1.
- I then use a while loop to multiply the numbers n,n-1,...,1.
- if the argument is 0, then the execution never enters the while loop.
- When the execution exits the while loop, the value of the variable factorial is equal to the factorial of n.
- I then prompt the user to enter a number and then I print the factorial of the number in the required format using a f-string and the function named factorial.

# Task 2

## Task 2: Using the Math Module for Calculations

### Problem Statement: Write a Python program that

    1.   Asks the user for a number as input.
    2.   Uses the math module to calculate the:
         o   Square root of the number
         o   Natural logarithm (log base e) of the number
         o   Sine of the number (in radians)
    3.   Displays the calculated results.

## Solution

- I import the math module.
- I then ask the user to input a number which I cast into float. I then assign this number to the variable x.
- I then print the sqrt, natural logarithm and the sine of "x" using the math module functions sqrt, log, and sin and suitable f-strings in the required format. Note that the the function math.log(x) returns the natural logarithm of x and the function math.sin(x) returns the sine of x, when x is in radians.

## Task 1

### Task 1: Perform Basic Mathematical Operations

**Problem Statement:** Write a Python program that does the following:

1. Takes two numbers as input from the user.
2. Performs the basic mathematical operations on these two numbers:
    o Addition
    o Subtraction
    o Multiplication
    o Division
3. Displays the results of each operation on the screen.

### Solution

- I used a docstring to include the problem statement in the program.
- Then I used input() with a suitable prompt string to input the numbers. The input which is a string is cast to int before being assigned to the variables n1, n2.
- I did not use float() to cast to float() as then the output would differ from the sample output. For example it will output 15.0 instead of 15 for the result of addition.
- I printed an empty string to print a blank line to create a one line gap between the input and the output.
- I used 4 separate print statements to output the results of the addition, subtraction, multiplication and division as in the sample output.

## Task 2

### Task 2: Create a Personalized Greeting

Problem Statement: Write a Python program that:

1. Takes a user's first name and last name as input.
2. Concatenates the first name and last name into a full name.
3. Prints a personalized greeting message using the full name.

### Solution

- I used a docstring to include the problem statement in the script.
- I input the first name and the last name into the variables first_name, last_name respectively using input() with the required prompt string.
- I then concatenated the strings first_name, ' ', and last_name into a third variable full_name using the "+" operator which in the case of strings concatenates strings. The ' ' was necessary to create a gap between the first and the last names.
- I then printed an empty string to print a blank line to create the gap between the input and the output.
- I then used a single print statement with the separator set to empty string to compose the output string and output it. This was necessary to print a '!' just after the full name, without any separation. This can also be achieved by appending '!' to the full_name, but I chose the previous method as I thought I should try to make use of the string formatting capabilities of the print() statement.

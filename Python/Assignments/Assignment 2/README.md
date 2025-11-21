# Task 1

## Task 1: Check if a Number is Even or Odd

### Problem Statement:  Write a Python program that

    1.  Takes an integer input from the user.
    2.  Checks whether the number is even or odd using an if-else statement.
    3.  Displays the result accordingly.

## Solution

- I prompt the user to "Enter a number" and cast the input from the user to an integer and assign it to the variable `num`.

- I then use a one-line if else statement.
- A one-line if else statement has the form:
    `(true expression) if (conditional expression) else (false expression)`
- the `conditional expression` in my script checks if the remainder when `num` is divided by `2` is `0`.
- the `true expression` in my script prints that the input number is even using a f-string.
- the `false expression` prints that the input number is odd using a f-string.
- So in line `20` first the `conditional expression` is evaluated, if it evaluates to `True`(`num` is even), then the `true expression` is evaluated, but if the `conditional expression` evaluates to `False`(`num` is odd), then the `false expression` is evaluated.

# Task 2

## Task 2: Sum of Integers from 1 to 50 Using a Loop

### Problem Statement: Write a Python program that

    1.   Uses a for loop to iterate over numbers from 1 to 50.
    2.   Calculates the sum of all integers in this range.
    3.   Displays the final sum.

## Solution

- I initialize a variable `sum` to `0`.
- I use a `for` loop in which the loop variable takes values from `1` to `50` as the iterator returned by `range(1,51)` gives values from `1` to `50`.
- in each iteration the value of the `sum` is incremented by the value of the loop variable `x`.
- at the culmination of the `for` loop, the sum of the numbers from `1` to `50` would have accumulated in the variable `sum`.
- finally the value of `sum` is printed in the required format using a f-string.

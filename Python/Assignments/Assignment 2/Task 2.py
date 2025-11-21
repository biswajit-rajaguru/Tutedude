"""

Task 2: Sum of Integers from 1 to 50 Using a Loop

Problem Statement: Write a Python program that:
    1.   Uses a for loop to iterate over numbers from 1 to 50.
    2.   Calculates the sum of all integers in this range.
    3.   Displays the final sum.

"""

# initialize the variable sum to 0
sum = 0

for x in range(1,51):  # range(a,b) iterates over the integers a,a+1,\ldots,b-1
    sum = sum + x

print(f"The sum of numbers from 1 to 50 is: {sum}")


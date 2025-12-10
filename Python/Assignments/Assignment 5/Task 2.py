'''
# Task 2: Demonstrate List Slicing 

## Problem Statement: Write a Python program that:
    1.   Creates a list of numbers from 1 to 10.
    2.   Extracts the first five elements from the list.
    3.   Reverses these extracted elements.
    4.   Prints both the extracted list and the reversed list
'''

# Create a list of 10 numbers 1..10
original_list = [x for x in range(1,11)]
print(f"Original list: {original_list}")

#Extracts the first five elements of the list.
extracted_first_five_elements = original_list[:5]
print(f"Extracted first five elements: {extracted_first_five_elements}")

#Reverses these extracted elements.
extracted_first_five_elements.reverse()
print(f"Reversed extracted elements: {extracted_first_five_elements}")


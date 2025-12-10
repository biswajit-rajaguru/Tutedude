'''
# Task 1: Create a Dictionary of Student Marks

## Problem Statement: Write a Python program that

1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.
'''

    #import create_marks_dictionary function from the module create_marks_dictionary
from create_marks_dictionary import create_marks_dictionary

try:
    # marks_dictionary  = the dictionary returned by create_marks_dictionary() 
    marks_dictionary = create_marks_dictionary()
    # if the marks_dictionary is None or empty dictionary rais an exception
    if marks_dictionary == None or marks_dictionary == {}:
        raise Exception("Failed to create Marks Dictionary")
except Exception as error:
    print(f"Error: {error}")
else:
    # if marks_dictionary have been successfully loaded/created 
    # use the procedure process_find_marks_request with marks_dictionary as the argument. 
    from find_marks_from_marks_dictionary import process_find_marks_request
    #Process a single request to retrieve marks
    process_find_marks_request(marks_dictionary)




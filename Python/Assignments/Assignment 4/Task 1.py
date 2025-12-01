"""
Task 1: Read a File and Handle Errors 

Problem Statement:  Write a Python program that:

    1.   Opens and reads a text file named sample.txt.
    2.   Prints its content line by line.
    3.   Handles errors gracefully if the file does not exist.
 
"""

# with the following line we can input the name of the file from the user
#file_name = input("File Name: ")

# But in the task statement it is given that the filename is "sample.txt" so we hardcode the file name 
file_name = "sample.txt"

# we use try-except-else-finally exception handling to open and read the file
try:
    with open(file_name, "rt") as fh:
        lines = fh.readlines()

# we handle the FileNotFoundException 
except FileNotFoundError as err:
    print(f'Error: The file "{file_name}" was not found.')

# we handle any exception that may occur during reading the file
except Exception:
    print(f'Error: Some error happened while reading the file "{file_name}"')

# we print the lines read from the file line by line in the else block
else:
    print("Reading file content: ")
    for index in range(len(lines)):
        print(f"Line {index+1}: {lines[index]}", end = '')

# we do not have any anything to do in the finally block as "with" already closes the file handle, so we just pass
finally:
    pass






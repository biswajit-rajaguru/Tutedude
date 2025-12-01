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

with open(file_name, "rt") as fh:
    lines = readlines(fh)




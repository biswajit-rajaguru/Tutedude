"""
Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
    1.   Takes user input and writes it to a file named output.txt.
    2.   Appends additional data to the same file.
    3.   Reads and displays the final content of the file.

"""

# we write the script as a sequence of three sub-scripts

# sub-script 1

# set the output_file_name
output_file_name = "output.txt"

#take input from the user
user_input = input("Enter text to write to the file: ")

# input() removes the terminating newline from the input. 
# But we need the terminating newline as we want to write lines to the output file output.txt.
# Without this when we write text to the file during append, the next line continues 
# on the same line as the previous line.
user_input += '\n'

# open the output file for writing in a "with" block and write the user input to the output file 
with open("output.txt", "wt") as of:
    of.write(user_input)

print(f"Data successfully written to {output_file_name}.")

# print a blank line to separate the interaction for the sub-script 2
print('')

# sub-script 2

# input additional text to be appended from the user.
additional_user_input = input("Enter additional text to append: ")

# input() removes the terminating newline from the input. 
# But we need the terminating newline as we want to write lines to the output file output.txt.
user_input += '\n'

#open the output file in append mode to append the additional text
with open("output.txt", "at") as of:
    of.write(additional_user_input)

print("Data successfully appended.")

#print a blankline to separate interaction for sub-script-3
print('')

#sub-script 3

# set the input-file name to the output-file name.
input_file_name = output_file_name

#open the input file for reading in a with block and read all the text 
with open(input_file_name, "rt") as inpf:
    input_from_file = inpf.read()

#print the contents of the input-file
print(f"Final content of {input_file_name}: ")
print(input_from_file)










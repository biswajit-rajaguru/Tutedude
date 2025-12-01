# Task 1

## Task 1: Read a File and Handle Errors

### Problem Statement:  Write a Python program that

    1.   Opens and reads a text file named sample.txt.
    2.   Prints its content line by line.
    3.   Handles errors gracefully if the file does not exist.

## Solution

- In the task statement the name of the file to be processed is given. So we hard coded the name of the file.
- But I have also added the option to input the name of the file to be processed from the user. This line is in commented state.
- I use a variable called file_name, that is set to the name of the file we process.
- I use try-except-else-finally exception handling to open and read the file.
- Specifically in the `try` block I open the file `sample.txt` for reading in text mode using `with` and read the file line by line using `readlines()` method of the file object `fh`, into the list `lines`.
- In the first except block we process the `FileNotFoundException` as specified in the task.
- In the second except block we process any exception that may occur during reading the file using the generic `Exception` class.
- In the else block we print the list of lines read from the file, keeping in mind that every line read from the file using readlines, has a terminating newline. So we change the `end` of the `print` statement to `''` to prevent a blank line from being printed.
- We do not have anything to do in the `finally` block, so we just `pass` in the `finally` block.

# Task 2

## Task 2: Write and Append Data to a File

### Problem Statement: Write a Python program that

        1.   Takes user input and writes it to a file named output.txt.
        2.   Appends additional data to the same file.
        3.   Reads and displays the final content of the file.

## Solution

- We write the script as a sequence of three sub-scripts.

- ### Sub-script 1

  - Set the output_file_name.
  - Take input from the user.
  - Input() removes the terminating newline from the input, so we add a terminating newline to the input so that "lines" get written to the output file.
  - Open the output file for writing in a `with` block and write the user input to the output file.

  - Print the notification `"Data successfully written to output.txt"`.
  - Print a blank line to separate the interaction for the sub-script 2.

- ### Sub-script 2

  - Input additional text to be appended from the user.
  - Add a terminating newline to the input as we want to write lines to the output file `output.txt`.
  - Open the output file in append mode to append the additional text in a `with` block and write additional text to `"output.txt"`.
  - Print the notification `"Data successfully appended."`
  - Print a blank line to separate the interaction for sub-script-3.

- ### Sub-script 3

  - Set the input-file name to the output-file name.
  - Open the input file for reading in a `with` block and `read` all the text.
  - Print the contents of the input-file in the specified format.

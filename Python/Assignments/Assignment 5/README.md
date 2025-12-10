# Task 1: Create a Dictionary of Student Marks

## Problem Statement: Write a Python program that

1. Creates a dictionary where student names are keys and their marks are values.
2. Asks the user to input a student's name.
3. Retrieves and displays the corresponding marks.
4. If the student’s name is not found, display an appropriate message.

## Solution

- we have created two modules:
  - `create_marks_dictionary.py`: from which we import the function `create_marks_dictionary()`. This function does not take any arguments. It prompts the user to enter the name and mark of each student and if the user signifies end of input by entering `"done"` or `Ctrl-d`, then it returns the marks_dictionary.
  - `find_marks_from_marks_dictionary.py`: from which we import the procedure `process_find_marks_request(marks_dictionary)`. This function takes a single argument, which is the marks_dictionary. This function prompts the user for a student name. If the student's name is in the marks dictionary then it prints the student's marks in the format specified in the assignment and if the student's name is not in the marks_dictionary, then it outputs `"Student not found"`. Finally it returns `"not_done"`, which is useful when iteratively asking for student's name. If the user enters `"done or Ctrl-d` then it returns "done".
  - in the `Task 1.py` program we first create a marks dictionary named `marks_dictionary` using the `create_marks_dictionary function`. We then process one request for retrieving a student's marks by calling the `find_marks_from_marks_dictionary` with the `marks_dictionary` as the argument.

## Alternate solution which differs from the specified workflow in Task 1

- In the workflow specified in the assignment we create a marks dictionary each time , and process one request.
- in this alternate workflow, we first run the script `"create_marks_dictionary.py"`. Here we create a marks dictionary, which is serialized and stored in a pickle file `"marks_list.pkl"`.
- then we run the script `"find_marks_from_marks_dictionary.py"` and it retrieves marks of multiple students in an interactive "session". We quit the session by pressing Ctrl-d or entering done for student name.
- This alternate workflow is added to the modules by putting it in the 'if __name__ == "__main__"' block of the two modules.

# Task 2: Demonstrate List Slicing

## Problem Statement: Write a Python program that

    1.   Creates a list of numbers from 1 to 10.
    2.   Extracts the first five elements from the list.
    3.   Reverses these extracted elements.
    4.   Prints both the extracted list and the reversed list

- Created the original list using list comprehension and the iterator `range(1,11)`
- Extracted the first five elements using slicing `original_list[:5]`
- reversed the list of extracted elements inplace using the list method reverse() `extracted_first_five_elements.reverse()`

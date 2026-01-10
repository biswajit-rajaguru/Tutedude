
def get_marks():
    
    # we employ a while loop to enter the marks to
    # allow for error handling if the input is not a number
    # in case the input is not a number then
    # a ValueError exception is raised during casting the input to float
    # We handle the error by discarding the input and 
    # reprompting the user for marks after an error message.
    while True:
        try:
            # we initially cast the marks to float to allow for partial marks and 
            # also to raise an exception if the input is not a number
            marks = float(input("Marks: "))
        except ValueError:
            print("Error: Marks should be a number")
            # incase of this exception we discard the input
            # and reprompt the user for marks
            continue
        # we allow for the possibility of the user signifying end of input by entering Ctrl-d
        # and if the user enters Ctrl-d then we return "done" for marks
        # which aborts the input cycle
        except EOFError:
            return "done"
        else:
            # the following "if" block casts marks to int if it is an integer or it keeps them as float
            # this is done to allow for parial marks and 
            # still print marks which are integers without a decimal point

            if marks == int(marks):
                marks = int(marks)
            # at this stage the marks are valid so return them 
            return marks
    

# the create marks_dictionary procedure creates the marks_dictionary
def create_marks_dictionary():
    # initialize the dictionary to an empty dictionary
    marks_dictionary = {}
    
    # take input for each student in a while loop
    print()

    # header display
    text1 = "Creating marks list"
    print(f"{text1}\n{'-' * len(text1)}")
    print(f"Enter student name and marks to add to the list \n")
    
    # We prompt the user for Student Name and Marks.
    # If the user enters done, then it 

    while True:
        #for better presentation we print a blank line at the start of each cycle
        print()
        print(f"Enter 'done' or Ctrl-d if there is no more input\n")
        try:
            name = input("Student Name: ")
        except EOFError:
            name = "done"
         
        if name == 'done':
            # we print a blank line to create a separation between the input cycle and the next output
            print()
            break
        # we imput the marks using the procedure get_marks()
        # which does some input validation
        # If the user aborts the input by pressing Ctrl-d then we process 
        # it by returning "done" from get_marks procedure
        # which then aborts the input cycle.

        marks = get_marks()
        if marks == "done":
            break
        marks_dictionary[name] = marks
    return marks_dictionary

if __name__ == "__main__":
    import pickle
    marks_dictionary = create_marks_dictionary()
    pickle_file_name = "marks_list.pkl"

    with open(pickle_file_name, "wb") as fh:
        pickle.dump(marks_dictionary, fh)

    print(f"Saved marks dictionary in '{pickle_file_name}'.")



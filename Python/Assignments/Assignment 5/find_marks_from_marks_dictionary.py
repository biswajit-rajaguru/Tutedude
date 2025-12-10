def process_find_marks_request(marks_dictionary):
    print()
    try:
        name = input("Enter the student's name(enter 'done' or Ctrl-d to exit): ")
    except EOFError:
        name = "done"
    if name in marks_dictionary:
        print(f"{name}'s marks: {marks_dictionary[name]}")
    elif name == "done":
        return "done"
    else:
        print("Student not found.")
    return "not_done"
    

def read_marks_dictionary_from_file(pickle_file_name):

    pickle_file_name = "marks_list.pkl"
    import pickle

    with open(pickle_file_name, "rb") as f:
        try:
            marks_dictionary = pickle.load(f)
        except EOFError:
            marks_dictionary = None
            print()
            print(f"'{pickle_file_name}' does not contain a marks dictionary.")
        else:
            print()
            print(f"Read marks dictionary from '{pickle_file_name}'.")

    return marks_dictionary

if __name__ == "__main__":
    pickle_file_name = "marks_list.pkl"
    marks_dictionary = read_marks_dictionary_from_file(pickle_file_name)
    if marks_dictionary == None:
        print(f"Error: Marks Dictionary could not be loaded")
    while process_find_marks_request(marks_dictionary) != done:
        pass
    print("bye!")

        




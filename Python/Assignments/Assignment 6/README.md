# Task

## Create a Calculator using tkinter

# Solution

## Files in the project

### There are two examples

    - example_using_calculator_widget_1.py
    - example_using_calculator_widget_2.py

```bash
python example_using_calculator_widget_1.py
```

### The widget consists of three files

    - CalculatorLogic.py - This implements the class CalculatorLogic
    - CalculatorUI.py    - This implements the class CalculatorUI
    - CalculatorWidget.py- This is the main widget module. we import the constructor `Calculator()` from it using 
      `from CalculatorWidget import Calculator`

### Theme files

        - basic_calculator_theme_file.json
        - cyberpunk_calculator_theme_file.json
        - retropop_calculator_theme_file.json
        - midnight_calculator_theme_file.json

## Design

### We have created a widget which implements a Calculator. We have created two examples

    - example_using_calculator_widget_1.py
    - example_using_calculator_widget_2.py
   that show example uses of the widget.

### The widget contains two classes CalculatorLogic and CalculatorUI that are implemented in

    - CalculatorLogic.py 
    - CalculatorUI.py

### To create an instance of a Calculator

        - we import the constructor function `Calculator()` from `CalculatorWidget` using `from CalculatorWidget import Calculator`
        - then we create an instance: `calculator = Calculator(parent, theme_file_name)`
            here - `parent` is the parent container of the calculator widget.
                 - `theme_file_name` is the name of a theme file, that can be given. This parameter is optional.
        - Finally the calculator widget is situated in the parent container. For example as `calculator.grid(row = 0, column = 0, sticky = "nsew")`
        - Though `pack` can be used on the Calculator widget, but it behaves best when the container uses `grid` layout.
        - A benefit of the Widget implementation is that multiple independent instances of the calculator widget can be used inside the same or different containers. This demoed in the 2nd example, where we have 4 independent calculator instances.
        - The Calculator widget is nonblocking and persists as long as the parent container exists. We have not implemented a method for the widget to quit, without effecting the parent. 

### CalculatorWidget.py defines the Calculator() constructor function

    In the Calculator() constructor function for the Calculator widget:
        - First an instance of the CalculatorLogic class is created, that maintains the calculator logic state, and provides a function `process_input` which is called by the on_key handler function which the UI calls to update the calculator logic, in response to a key press.
        - The Calculator logic consists of:
            - Its state variables: 
                - _expression:  that holds the arithmetic expression on the display. It is a string.
                - _last_result: that holds the value of the last evaluated result. It is also a string.
                - _entering_expression: this is a boolean variable which tells whether we are currently inputting an expression or not.
                - _memory: this is a number and is the value that is currently in memory.
            - its key handlers:
                - `_digit_or_dot()` that handles a digit or . key press
                - `_operator()` that handles `+,-,*,/` keys
                - `_evaluate()` that handles `=` key
                - `_clear(all = False)` that handles `C`, `AC` keys
                - `_Moperator()` that handle "M+", "M-", "MR", "MC" keys
        - the Calculatorlogic has a public method `process_input` that is called by the on_key function with argument which is equal to the label of the key pressed
        - the process_input method then calls the appropriate key_handler
        - the key handler update the logic state variables depending upon the key that was pressed 
        - the process input then returns the value of the `_expression` state variable to the `on_key` function        
        - the on_key handler uses it to set the display of the calculator using the `set_display` public method of the ui instance.
                
                                
        - then we define the on_key function
            - it takes a string parameter named `key`, which the string label or name of the key that is pressed.
            - it then calls the `process_input` public method of the logic instance. 
            - the process_input updates the calculator state and return the value of the current expression that should be on the display.
            - it then calls the `set_display` public method of the UI instance to set the display of the calculator UI.
            - this function is is the *"wiring"* between the calculator Logic and the calculator UI.

        - Then `ui = CalculatorUI(parent, on_key, theme_file_name)` creates an instance of the calculatorUI
        - Here parent is the parent container which contains the Calcuator widget. The parent can be root or it can be a frame in a tkinter application.
        - the theme file name is the name of json file along with the `.json` extension that contains colors for the 
            - display_bg
            - keypad_bg
            - display_main_label_bg
            - display_main_label_fg
            - key_bg
            - key_fg
          that are color strings in the "#rrggbb" format, which are used to set the foreground and background attribrutes of various tkinter widgets constituting the calculator UI.
          We have provided four such example theme files.
        - the on_key is the function is the one we just defined.
        - The construct returns the ui instance created 

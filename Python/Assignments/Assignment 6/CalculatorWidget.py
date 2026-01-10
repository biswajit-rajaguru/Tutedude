
from CalculatorUI import CalculatorUI
from CalculatorLogic import CalculatorLogic

def Calculator(parent, theme_file = "basic_calculator_theme_file.json"):
    
    # this is the instance of Calculator Logic that will implement the Calculator Logic.
    logic = CalculatorLogic()
    
    #this is the event handler function that the ui calls to process the key press event
    def on_key(key):
        
        # the UI keys have "×","÷" strings on two keys, which we map to strings "*", "/" so that
        # the expression is a valid python arithmetic expression string,
        # that can be exaluated by the eval function

        key_map = {"×": "*", "÷": "/"}
        
        # the key_map.get(key,key) processes the strings "×", "÷" while passing the other key names unchanged
        # the value returned by the process_input method is the display string after the keypress
        value = logic.process_input(key_map.get(key, key))
        # ui.set_display displays the display string in the ui's display label widget properly. 
        ui.set_display(value)

    ui = CalculatorUI(parent, on_key=on_key, theme_file = theme_file)
    
    return ui
    
    

    


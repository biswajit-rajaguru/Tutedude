from CalculatorUI import CalculatorUI
from CalculatorLogic import CalculatorLogic


def Calculator(parent):
    
    logic = CalculatorLogic()

    def handle_key(key):
        key_map = {"×": "*", "÷": "/"}
        value = logic.process_input(key_map.get(key, key))
        ui.set_display(value)

    ui = CalculatorUI(parent, on_key=handle_key)
    return ui

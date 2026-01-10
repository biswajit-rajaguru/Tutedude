class CalculatorLogic:
    def __init__(self):

        # it is the expression that is displayed in the "display" of the calculator 
        self._expression = "" 
        
        self._last_result = "" # it is last result we got
        
        # The calculator has two states:
        # 1. when it is entering or inputting an expression to evaluate
        # 2. when it is displaying a result
        # entering_expression is true if the calculator is inputting expression or else it is False.
        self._entering_expression = True 
        
        # memory is variable which stores the value currently in memory. It is supposed to be a number.
        self._memory = 0

    # process input is the key handler which changes the calculator state based on the key press on the UI
    # it is passed as the on_key event handler when creating the CalcultorUI instance
    def process_input(self, key):
        # key is a string 
        # it is the name of the key 
        # it is same as the one visible on the key text
        
        # Depending upon the key we call their respective key handlers
        # They change the state of the calculator and update the expression.
        # The expression after the key is processed is returned. 

        if key.isdigit() or key == ".":
            self._digit_or_dot(key)
        elif key in "+-*/":
            self._operator(key)
        elif key == "=":
            self._evaluate()
        elif key == "C":
            self._clear(all = False)
        elif key == "AC":
            self._clear(all = True)
        elif key in ["M+", "M-", "MR", "MC"]:
            self._Moperator(key)
        return self._expression if self._expression else "0"

    
    def _digit_or_dot(self, key):
            # when a digit or dot is entered and we not entering a expression, then we clear the display
            # and start entering a new expression
            # but if we are entering an expression we just append the key or dot to the end of the display.

            if not self._entering_expression:
                self._expression = ""
                self._entering_expression = True
            # if the number that is currently ebeing entered already has dot, then we ignore the dot input
            # _current_number() returns the number that is being entered or "" if no number is being entered
            if key == "." and "." in self._current_number():
                return
            # appending the key to end of the expression
            self._expression += key

    def _operator(self, key):
        if not self._expression and self._last_result:
            self._expression = self._last_result

        # suppose we enter two operators in succession, then all operators except the last one are discarded
        if self._expression and self._expression[-1] in "+-*/":
            self._expression = self._expression[:-1]

        self._expression += key 
        # we make sure that we are in entering expression mode after we enter an operator.
        self._entering_expression = True

    @staticmethod
    def _string_representation_of_the_number(value):
        # value is supposed to be a number
        s = "" # the string to be returned 
        if value % 1 == 0: # if value does not have a decimal part, represent it as an integer, without decimal point
            s = str(int(value))
        else:
            s = f"{value:.2f}"
        return s 
        
    def _Moperator(self, key):

        try:

            evaluation_result = eval(self._expression)
            if not isinstance(evaluation_result, (int, float)):
                evaluation_result = 0
        except Exception:
            self._clear(all = True)
            return
        
        if key == "M+":
            self._memory += evaluation_result
        elif key == "M-":
            self._memory -= evaluation_result
        elif key == "MC":
            self._memory = 0
        elif key == "MR":
            try:
                self._expression = CalculatorLogic._string_representation_of_the_number(self._memory)
                self._entering_expression = True if self._expression != "0" else False
            except Exception:
                self._clear(all = True)
    

    def _evaluate(self):
        try:
            result = eval(self._expression)
            self._last_result = self._string_representation_of_the_number(result)
            self._expression = self._last_result
            self._entering_expression = False
        except Exception:
            self._clear(all=True)

    def _clear(self, all=False):
        self._expression = ""
        if all:
            self._last_result = ""
        self._entering_expression = True

    def _current_number(self):
        num = ""
        for c in reversed(self._expression):
            if c in "+-*/":
                break
            num = c + num
        return num
        

        




        










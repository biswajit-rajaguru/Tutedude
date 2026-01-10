# CalculatorLogic.py

class CalculatorLogic:
    def __init__(self):
        self.expression = ""
        self.last_result = ""
        self.entering_expression = True
        self.memory = 0

    def process_input(self, key):
        if key.isdigit() or key == ".":
            self._digit_or_dot(key)
        elif key in "+-*/":
            self._operator(key)
        elif key == "=":
            self._evaluate()
        elif key == "C":
            self._clear(all=False)
        elif key == "AC":
            self._clear(all=True)
        elif key in ["M+", "M-", "MR", "MC"]:
            self._Moperator(key)

        return self.expression if self.expression else "0"

    def _digit_or_dot(self, key):
        if not self.entering_expression:
            self.expression = ""
            self.entering_expression = True

        if key == "." and "." in self._current_number():
            return

        self.expression += key

    def _operator(self, key):
        if not self.expression and self.last_result:
            self.expression = self.last_result

        if self.expression and self.expression[-1] in "+-*/":
            self.expression = self.expression[:-1]

        self.expression += key
        self.entering_expression = True

    @staticmethod
    def displaynumber(value):
        s = ""
        if value % 1 == 0:
            s = str(int(value))
        else:
            s = f"{value:.2f}" 
        return s
    
    def _Moperator(self, key):
        try:
            number_on_display = eval(self.expression)
            if not isinstance(number_on_display, (int, float)):
                number_on_display = 0
        except Exception:
            self._clear(all = True)
            return
        
        
        if key == "M+":
            self.memory += number_on_display
        elif key == "M-":
            self.memory -= number_on_display
        elif key == "MC":
            self.memory = 0.0
        elif key == "MR":
            try:
                self.expression = CalculatorLogic.displaynumber(self.memory)
                self.entering_expression = True if self.expression != "0" else False
            except Exception:
                self._clear(all = True)
    

    def _evaluate(self):
        try:
            result = eval(self.expression)
            self.last_result = self.displaynumber(result)
            self.expression = self.last_result
            self.entering_expression = False
        except Exception:
            self._clear(all=True)

    def _clear(self, all=False):
        self.expression = ""
        if all:
            self.last_result = ""
        self.entering_expression = True

    def _current_number(self):
        num = ""
        for c in reversed(self.expression):
            if c in "+-*/":
                break
            num = c + num
        return num

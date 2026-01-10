
# CalculatorUI.py
# Calculator UI module

import tkinter as tk
import tkinter.font as tkfont
import json

# we define a custom button class for the calculator keys
# that doesnot change color on focus, has a custom font, and has a flat appearence
class _CalculatorKey(tk.Button):

    def __init__(self, master = None, font = None, **kwargs):

        # as we are extending the tk.Button class
        # we should call its constructor first so that it sets up
        # things we inherit from the base class
        super().__init__(master, **kwargs)

        self.configure(
            relief = "flat",
            highlightthickness = 0,
            activebackground = self.cget("bg"),
            activeforeground = self.cget("fg"),
            font = font,
        )
        

# the Calculator is built as tkinter widget that extends the tkinter Frame widget

class CalculatorUI(tk.Frame):
    def __init__(self, master, on_key, theme_file = "basic_calculator_theme.json"):
        
        #the base class is initialized first so that
        # it sets up the inherited things 
        super().__init__(master)
        

        # on_key is the event handler function that
        # handles key presses on the UI 
        # this is passed to the CalculatorUI constructor
        # during its initialization.
        self._on_key = on_key
        self._load_theme_file(theme_file)
        # we now create two tkinter font objects 
        # that are to be used a s the fonts for the display
        # and the font for the key 
        self._displayFont = tkfont.Font(
            root = master, 
            family = "Helvetica",
            size = 24)
        self._keyFont  = tkfont.Font(
            root = master,
            family = "Helvetica",
            size = 14,
            weight = "bold")
        self._build_ui()
        self._bind_resize()

    
    def _load_theme_file(self, theme_file):
        # Default fallback values in case the file is missing or broken
        default_theme = {
            "display_bg": "#000000", 
            "keypad_bg": "#222222",
            "display_main_label_bg": "#000000", 
            "display_main_label_fg": "#ffffff",
            "key_bg": "#444444",
            "key_fg": "#ffffff",
            "reset_key_bg": "#ffffff",
            "reset_key_fg": "#000000",
        }

        try:
            with open(theme_file, 'r') as f:
                theme = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Warning: Could not load {theme_file}. Using default theme.")
            theme = default_theme

        # Assign values to instance variables as requested
        self._display_bg = theme.get("display_bg", default_theme["display_bg"])
        self._keypad_bg = theme.get("keypad_bg", default_theme["keypad_bg"])
        self._display_main_label_bg = theme.get("display_main_label_bg", default_theme["display_main_label_bg"])
        self._display_main_label_fg = theme.get("display_main_label_fg", default_theme["display_main_label_fg"])
        self._key_bg = theme.get("key_bg", default_theme["key_bg"])
        self._key_fg = theme.get("key_fg", default_theme["key_fg"])
        self._reset_key_bg = theme.get("reset_key_bg", default_theme["reset_key_bg"])
        self._reset_key_fg = theme.get("reset_key_fg", default_theme["reset_key_fg"])
    
    # _build_ui is the principal procedure that builds the UI
    def _build_ui(self):
        
        # CalculatorUI is an extension of the frame widget 
        # within which the calculator lives
        # within this widget we use the grid layout 
        # the outermost grid has two cells
        # the top cell which hold the display which is a frame widget
        # below the display the space is a cell which holds a frame widget
        # this frame is partitoned to two cells vertically that hold two
        # blocks of keys
        
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 3)
        self.columnconfigure(0, weight = 1)

        display = tk.Frame(self, bg = self._display_bg)
        keypad  = tk.Frame(self, bg = self._keypad_bg)
        
        display.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
        keypad.grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
        
        #the display is frame because it is supposed to be extended to contain may
        # different labels to show various things on the calculator display
        # in various fonts. but for now it contains a single label widget
        display.rowconfigure(0, weight = 1)
        display.columnconfigure(0, weight = 1)

        self._display_main_label = tk.Label(
            display,                     # parent
            text = "0",                  # default display text
            anchor = "e",                # text is vertically centered in the label and right-aligned
            bg = self._display_main_label_bg, # background color of the main label
            fg = self._display_main_label_fg, # foreground color of the main level
            font = self._displayFont,
        )

        self._display_main_label.grid(row = 0, column = 0, sticky = "nsew")

        # the comosotion of the keypad is complicated
        # so we wrap it in a procedure
        self._build_keypad(keypad)

    def _build_keypad(self, keypad):
        # the keypad frame is divided vertically into two frames vertically
        keypad.rowconfigure(0, weight = 1)
        keypad.columnconfigure(0, weight = 1)
        keypad.columnconfigure(1, weight = 1)

        digits = tk.Frame(keypad)
        digits.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
        operators = tk.Frame(keypad)
        operators.grid(row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)

        # the frames digits and operator have the same grid structure
        # so we configure the two grids simulateneously

        for i in range(4):
            digits.rowconfigure(i, weight = 1)
            operators.rowconfigure(i, weight = 1)
        
        for j in range(3):
            digits.columnconfigure(j, weight = 1)
            operators.columnconfigure(j, weight = 1)

        # Now we create the keys in digits block
        # the following creates the first three rows in the digits block
        for i, text in enumerate("789456123"):
            self._key(digits, text).grid(row = i//3, column = i%3, sticky = "nsew", padx = 5, pady = 5)
        
        # column span = 2 means that, that  cell will span over 2 grid cells.
        self._key(digits, "0").grid(row = 3, column = 0, columnspan = 2, sticky = "nsew", padx = 5, pady = 5) 
        self._key(digits, ".").grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5) 

        # now we create the operators block
        #
        for i, text in enumerate(["M+", "M-", "MR", "×", "÷", "MC"]):
            self._key(operators, text).grid(row = i//3, column = i%3, sticky = "nsew", padx = 5, pady = 5)
        
        # rowspan = 2 => the cell spans over two rows vertically
        self._key(operators, "+").grid(row = 2, column = 0, rowspan = 2, sticky = "nsew", padx = 5, pady = 5) 
        self._key(operators, "-").grid(row = 2, column = 1, sticky = "nsew", padx = 5, pady = 5) 
        self._key(operators, "=").grid(row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5) 
        self._key(operators, "C", reset = True).grid(row = 2, column = 2, sticky = "nsew", padx = 5, pady = 5) 
        self._key(operators, "AC", reset = True).grid(row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5) 
        
        
    def _key(self, parent, text, reset = False):
        bg = self._key_bg if not reset else self._reset_key_bg
        fg = self._key_fg if not reset else self._reset_key_fg
        return _CalculatorKey(
            parent,
            text = text,
            bg = bg,
            fg = fg,
            command = lambda t = text: self._on_key(t),
            font = self._keyFont
        )
    def _bind_resize(self):
        self.bind("<Configure>", self._resize, add = True)
    
    def _resize(self, event):
        cellHeight = event.height / 5
        self._keyFont.configure(size = max(8, int(cellHeight * 0.3)))
        self._displayFont.configure(size = max(12, int(cellHeight * 0.5)))
    
    # this function is called by CalculatorLogic instance to update the display
    # calling this function is the only interaction Calculator Logic has with Calculator UI

    def set_display(self, value):
        self._display_main_label.configure(text = value)





            


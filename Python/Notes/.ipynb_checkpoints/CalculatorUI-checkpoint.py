# CalculatorUI.py

import tkinter as tk
import tkinter.font as tkfont


class CalculatorButton(tk.Button):
    #buttonFont = tkfont.Font(family="Helvetica", size=14, weight="bold")

    def __init__(self, master=None, font = None, **kwargs):

        super().__init__(master, **kwargs)
        
        # if not hasattr(master, "_button_font"):
        #     master._button_font = tkfont.Font(
        #         root=self.winfo_toplevel(),
        #         family="Helvetica",
        #         size=14,
        #         weight="bold"
        #     )
        #kwargs.setdefault("font", master._button_font)
        

        self.configure(
            relief="flat",
            highlightthickness=0,
            activebackground=self.cget("bg"),
            activeforeground=self.cget("fg"),
            font = font,
        )


class CalculatorUI(tk.Frame):
    def __init__(self, master, on_key):
        super().__init__(master)
        self.on_key = on_key

        self.displayFont = tkfont.Font(root = master, family="Helvetica", size=24)
        self._button_font = tkfont.Font(
                root= master,
                family="Helvetica",
                size=14,
                weight="bold"
            )
        self._build_ui()
        self._bind_resize()

    def _build_ui(self):
        #self.grid(sticky="nsew")

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=3)
        self.columnconfigure(0, weight=1)

        display = tk.Frame(self, bg="#b3ffec")
        keypad = tk.Frame(self, bg="#cccccc")

        display.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        keypad.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        display.rowconfigure(0, weight=1)
        display.columnconfigure(0, weight=1)

        self.display_label = tk.Label(
            display,
            text="0",
            anchor="e",
            bg="#b3ffec",
            fg="#001a00",
            font=self.displayFont,
        )
        self.display_label.grid(sticky="nsew")

        self._build_keypad(keypad)

    def _build_keypad(self, keypad):
        digits = tk.Frame(keypad)
        ops = tk.Frame(keypad)

        digits.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        ops.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        keypad.rowconfigure(0, weight=1)
        keypad.columnconfigure(0, weight=1)
        keypad.columnconfigure(1, weight=1)

        for i in range(4):
            digits.rowconfigure(i, weight=1)
            ops.rowconfigure(i, weight=1)

        for j in range(3):
            digits.columnconfigure(j, weight=1)
            ops.columnconfigure(j, weight=1)

        for i, text in enumerate("789456123"):
            self._btn(digits, text).grid(row=i//3, column=i%3, sticky="nsew", padx=5, pady=5)

        self._btn(digits, "0").grid(row=3, column=0, columnspan=2, sticky="nsew", padx=5, pady=5)
        self._btn(digits, ".").grid(row=3, column=2, sticky="nsew", padx=5, pady=5)

        for i, text in enumerate(["M+", "M-", "MR", "×", "÷", "MC"]):
            self._btn(ops, text).grid(row=i//3, column=i%3, sticky="nsew", padx=5, pady=5)

        self._btn(ops, "+").grid(row=2, column=0, rowspan=2, sticky="nsew", padx=5, pady=5)
        self._btn(ops, "-").grid(row=2, column=1, sticky="nsew", padx=5, pady=5)
        self._btn(ops, "=").grid(row=3, column=1, sticky="nsew", padx=5, pady=5)
        self._btn(ops, "C", reset=True).grid(row=2, column=2, sticky="nsew", padx=5, pady=5)
        self._btn(ops, "AC", reset=True).grid(row=3, column=2, sticky="nsew", padx=5, pady=5)

    def _btn(self, parent, text, reset=False):
        bg = "white" if reset else "#8c8c8c"
        fg = "#444444" if reset else "#e6e6e6"
        return CalculatorButton(
            parent,
            text=text,
            bg=bg,
            fg=fg,
            command=lambda t=text: self.on_key(t),
            font = self._button_font
        )

    def _bind_resize(self):
        self.bind("<Configure>", self._resize, add=True)

    def _resize(self, event):
        cell = event.height / 5
        self._button_font.configure(size=max(8, int(cell * 0.3)))
        self.displayFont.configure(size=max(12, int(cell * 0.5)))

    def set_display(self, value):
        self.display_label.config(text=value)

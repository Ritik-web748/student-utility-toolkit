import tkinter as tk


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Basic Calculator")
        self.geometry("320x420")
        self.minsize(320, 420)
        self.configure(bg="#f3f3f3")

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self._build_ui()

    def _build_ui(self):
        display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Arial", 28),
            bg="#ffffff",
            fg="#111111",
            bd=0,
            justify="right",
            state="readonly",
            readonlybackground="#ffffff",
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=12, pady=(12, 8), ipady=18)

        buttons = [
            ("C", 1, 0, "#d9d9d9"),
            ("(", 1, 1, "#d9d9d9"),
            (")", 1, 2, "#d9d9d9"),
            ("/", 1, 3, "#ff9f0a"),
            ("7", 2, 0, "#f0f0f0"),
            ("8", 2, 1, "#f0f0f0"),
            ("9", 2, 2, "#f0f0f0"),
            ("*", 2, 3, "#ff9f0a"),
            ("4", 3, 0, "#f0f0f0"),
            ("5", 3, 1, "#f0f0f0"),
            ("6", 3, 2, "#f0f0f0"),
            ("-", 3, 3, "#ff9f0a"),
            ("1", 4, 0, "#f0f0f0"),
            ("2", 4, 1, "#f0f0f0"),
            ("3", 4, 2, "#f0f0f0"),
            ("+", 4, 3, "#ff9f0a"),
            ("0", 5, 0, "#f0f0f0", 2),
            (".", 5, 2, "#f0f0f0"),
            ("=", 5, 3, "#ff9f0a"),
        ]

        for button in buttons:
            text = button[0]
            row = button[1]
            col = button[2]
            color = button[3]
            colspan = button[4] if len(button) > 4 else 1

            tk.Button(
                self,
                text=text,
                font=("Arial", 20, "bold"),
                bg=color,
                fg="#111111" if color in ["#d9d9d9", "#f0f0f0"] else "#ffffff",
                bd=0,
                command=lambda value=text: self.handle_click(value),
                padx=20,
                pady=18,
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=4, pady=4)

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

    def handle_click(self, value):
        if value == "C":
            self.expression = ""
            self.display_var.set("0")
            return

        if value == "=":
            self.calculate()
            return

        if value in ["+", "-", "*", "/", "(", ")", "."]:
            self.expression += value
        else:
            self.expression += str(value)

        self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression, {"__builtins__": {}}, {})
            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            self.expression = ""
            self.display_var.set("Cannot divide by zero")
        except Exception:
            self.expression = ""
            self.display_var.set("Error")


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()

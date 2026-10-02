import tkinter as tk
from tkinter import messagebox


class TemperatureConverter(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window settings
        self.title("Temperature Converter")
        self.geometry("420x520")
        self.minsize(420, 520)
        self.configure(bg="#f3f3f3")

        self.create_ui()

    def create_ui(self):

        # ==========================================
        # TITLE
        # ==========================================

        title = tk.Label(
            self,
            text="Temperature Converter",
            font=("Segoe UI", 24, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self,
            text="Convert between Celsius, Fahrenheit and Kelvin",
            font=("Segoe UI", 10),
            bg="#f3f3f3",
            fg="#666666"
        )

        subtitle.pack(pady=(0, 20))

        # ==========================================
        # CONVERSION TYPE
        # ==========================================

        conversion_label = tk.Label(
            self,
            text="Conversion",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        conversion_label.pack(pady=(5, 8))

        self.conversion_var = tk.StringVar(
            value="Celsius → Fahrenheit"
        )

        conversion_options = [
            "Celsius → Fahrenheit",
            "Fahrenheit → Celsius",
            "Celsius → Kelvin",
            "Kelvin → Celsius",
            "Fahrenheit → Kelvin",
            "Kelvin → Fahrenheit"
        ]

        conversion_menu = tk.OptionMenu(
            self,
            self.conversion_var,
            *conversion_options
        )

        conversion_menu.config(
            font=("Segoe UI", 11),
            bg="white",
            fg="#111111",
            activebackground="#e6e6e6",
            activeforeground="#111111",
            bd=0,
            highlightthickness=0,
            width=24,
            pady=8
        )

        conversion_menu["menu"].config(
            font=("Segoe UI", 11),
            bg="white",
            fg="#111111"
        )

        conversion_menu.pack(
            pady=(0, 20)
        )

        # ==========================================
        # INPUT
        # ==========================================

        input_label = tk.Label(
            self,
            text="Enter Temperature",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        input_label.pack(pady=(5, 8))

        self.temperature_entry = tk.Entry(
            self,
            font=("Segoe UI", 20),
            bg="white",
            fg="#111111",
            bd=0,
            justify="center"
        )

        self.temperature_entry.pack(
            padx=45,
            fill="x",
            ipady=10
        )

        # ==========================================
        # BUTTONS
        # ==========================================

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )

        button_frame.pack(
            pady=25
        )

        convert_button = tk.Button(
            button_frame,
            text="Convert",
            font=("Segoe UI", 12, "bold"),
            bg="#ff9f0a",
            fg="white",
            activebackground="#e58d00",
            activeforeground="white",
            bd=0,
            padx=30,
            pady=10,
            cursor="hand2",
            command=self.convert_temperature
        )

        convert_button.pack(
            side="left",
            padx=5
        )

        clear_button = tk.Button(
            button_frame,
            text="Clear",
            font=("Segoe UI", 12),
            bg="#d9d9d9",
            fg="#111111",
            activebackground="#c5c5c5",
            activeforeground="#111111",
            bd=0,
            padx=30,
            pady=10,
            cursor="hand2",
            command=self.clear
        )

        clear_button.pack(
            side="left",
            padx=5
        )

        # ==========================================
        # RESULT
        # ==========================================

        result_label = tk.Label(
            self,
            text="RESULT",
            font=("Segoe UI", 10, "bold"),
            bg="#f3f3f3",
            fg="#777777"
        )

        result_label.pack(
            pady=(5, 5)
        )

        self.result = tk.Label(
            self,
            text="--",
            font=("Segoe UI", 28, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        self.result.pack(
            pady=5
        )

    # ==========================================
    # CONVERSION LOGIC
    # ==========================================

    def convert_temperature(self):

        # Get the value from Entry
        value = self.temperature_entry.get().strip()

        # Check for empty input
        if value == "":
            messagebox.showerror(
                "Missing Input",
                "Please enter a temperature."
            )
            return

        # Convert input to a number
        try:
            temperature = float(value)

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number."
            )
            return

        # Get selected conversion
        conversion = self.conversion_var.get()

        # ==========================================
        # CELSIUS → FAHRENHEIT
        # ==========================================

        if conversion == "Celsius → Fahrenheit":

            result = (temperature * 9 / 5) + 32

            self.result.config(
                text=f"{result:.2f} °F"
            )

        # ==========================================
        # FAHRENHEIT → CELSIUS
        # ==========================================

        elif conversion == "Fahrenheit → Celsius":

            result = (temperature - 32) * 5 / 9

            self.result.config(
                text=f"{result:.2f} °C"
            )

        # ==========================================
        # CELSIUS → KELVIN
        # ==========================================

        elif conversion == "Celsius → Kelvin":

            result = temperature + 273.15

            if result < 0:
                messagebox.showerror(
                    "Invalid Temperature",
                    "Temperature cannot be below absolute zero."
                )
                return

            self.result.config(
                text=f"{result:.2f} K"
            )

        # ==========================================
        # KELVIN → CELSIUS
        # ==========================================

        elif conversion == "Kelvin → Celsius":

            if temperature < 0:
                messagebox.showerror(
                    "Invalid Temperature",
                    "Kelvin cannot be less than 0."
                )
                return

            result = temperature - 273.15

            self.result.config(
                text=f"{result:.2f} °C"
            )

        # ==========================================
        # FAHRENHEIT → KELVIN
        # ==========================================

        elif conversion == "Fahrenheit → Kelvin":

            result = (
                (temperature - 32) * 5 / 9
            ) + 273.15

            if result < 0:
                messagebox.showerror(
                    "Invalid Temperature",
                    "Temperature cannot be below absolute zero."
                )
                return

            self.result.config(
                text=f"{result:.2f} K"
            )

        # ==========================================
        # KELVIN → FAHRENHEIT
        # ==========================================

        elif conversion == "Kelvin → Fahrenheit":

            if temperature < 0:
                messagebox.showerror(
                    "Invalid Temperature",
                    "Kelvin cannot be less than 0."
                )
                return

            result = (
                (temperature - 273.15) * 9 / 5
            ) + 32

            self.result.config(
                text=f"{result:.2f} °F"
            )

    # ==========================================
    # CLEAR
    # ==========================================

    def clear(self):

        self.temperature_entry.delete(
            0,
            tk.END
        )

        self.conversion_var.set(
            "Celsius → Fahrenheit"
        )

        self.result.config(
            text="--"
        )


# ==============================================
# START PROGRAM
# ==============================================

if __name__ == "__main__":

    app = TemperatureConverter()

    app.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox


class PercentageCalculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Percentage Calculator")
        self.geometry("420x500")
        self.minsize(420, 500)
        self.configure(bg="#f3f3f3")

        self.create_ui()

    def create_ui(self):

        # -------------------------------
        # Title
        # -------------------------------

        title = tk.Label(
            self,
            text="Percentage Calculator",
            font=("Segoe UI", 24, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        title.pack(pady=(25, 20))

        # -------------------------------
        # Calculation type
        # -------------------------------

        type_label = tk.Label(
            self,
            text="Choose calculation:",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3"
        )

        type_label.pack()

        self.calculation_type = ttk.Combobox(
            self,
            values=[
                "Marks to Percentage",
                "Percentage Increase",
                "Percentage Decrease"
            ],
            state="readonly",
            font=("Segoe UI", 11)
        )

        self.calculation_type.current(0)
        self.calculation_type.pack(
            padx=40,
            pady=10,
            fill="x"
        )

        self.calculation_type.bind(
            "<<ComboboxSelected>>",
            self.update_labels
        )

        # -------------------------------
        # First input
        # -------------------------------

        self.first_label = tk.Label(
            self,
            text="Obtained Marks",
            font=("Segoe UI", 12),
            bg="#f3f3f3"
        )

        self.first_label.pack(
            anchor="w",
            padx=40,
            pady=(15, 5)
        )

        self.first_entry = tk.Entry(
            self,
            font=("Segoe UI", 14),
            justify="center"
        )

        self.first_entry.pack(
            padx=40,
            fill="x"
        )

        # -------------------------------
        # Second input
        # -------------------------------

        self.second_label = tk.Label(
            self,
            text="Total Marks",
            font=("Segoe UI", 12),
            bg="#f3f3f3"
        )

        self.second_label.pack(
            anchor="w",
            padx=40,
            pady=(15, 5)
        )

        self.second_entry = tk.Entry(
            self,
            font=("Segoe UI", 14),
            justify="center"
        )

        self.second_entry.pack(
            padx=40,
            fill="x"
        )

        # -------------------------------
        # Calculate button
        # -------------------------------

        calculate_button = tk.Button(
            self,
            text="Calculate",
            font=("Segoe UI", 14, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=20,
            pady=12,
            command=self.calculate
        )

        calculate_button.pack(
            padx=40,
            pady=25,
            fill="x"
        )

        # -------------------------------
        # Result
        # -------------------------------

        result_title = tk.Label(
            self,
            text="Result",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3"
        )

        result_title.pack()

        self.result_label = tk.Label(
            self,
            text="Enter values and click Calculate",
            font=("Segoe UI", 18, "bold"),
            bg="#ffffff",
            fg="#111111",
            padx=20,
            pady=20
        )

        self.result_label.pack(
            padx=40,
            pady=10,
            fill="x"
        )

        # -------------------------------
        # Clear button
        # -------------------------------

        clear_button = tk.Button(
            self,
            text="Clear",
            font=("Segoe UI", 11),
            command=self.clear_fields
        )

        clear_button.pack(pady=5)

    # --------------------------------------------------
    # Change labels depending on calculation type
    # --------------------------------------------------

    def update_labels(self, event=None):

        calculation = self.calculation_type.get()

        if calculation == "Marks to Percentage":

            self.first_label.config(text="Obtained Marks")
            self.second_label.config(text="Total Marks")

        elif calculation == "Percentage Increase":

            self.first_label.config(text="Old Value")
            self.second_label.config(text="New Value")

        elif calculation == "Percentage Decrease":

            self.first_label.config(text="Old Value")
            self.second_label.config(text="New Value")

    # --------------------------------------------------
    # Perform calculation
    # --------------------------------------------------

    def calculate(self):

        try:

            first = float(self.first_entry.get())
            second = float(self.second_entry.get())

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers."
            )

            return

        calculation = self.calculation_type.get()

        # ----------------------------------------------
        # Marks to Percentage
        # ----------------------------------------------

        if calculation == "Marks to Percentage":

            obtained = first
            total = second

            if total <= 0:

                messagebox.showerror(
                    "Invalid Input",
                    "Total marks must be greater than 0."
                )

                return

            if obtained < 0:

                messagebox.showerror(
                    "Invalid Input",
                    "Obtained marks cannot be negative."
                )

                return

            if obtained > total:

                messagebox.showerror(
                    "Invalid Input",
                    "Obtained marks cannot be greater than total marks."
                )

                return

            percentage = (obtained / total) * 100

            self.result_label.config(
                text=f"{percentage:.2f}%"
            )

        # ----------------------------------------------
        # Percentage Increase
        # ----------------------------------------------

        elif calculation == "Percentage Increase":

            old_value = first
            new_value = second

            if old_value <= 0:

                messagebox.showerror(
                    "Invalid Input",
                    "Old value must be greater than 0."
                )

                return

            increase = (
                (new_value - old_value)
                / old_value
            ) * 100

            self.result_label.config(
                text=f"{increase:.2f}% Increase"
            )

        # ----------------------------------------------
        # Percentage Decrease
        # ----------------------------------------------

        elif calculation == "Percentage Decrease":

            old_value = first
            new_value = second

            if old_value <= 0:

                messagebox.showerror(
                    "Invalid Input",
                    "Old value must be greater than 0."
                )

                return

            decrease = (
                (old_value - new_value)
                / old_value
            ) * 100

            self.result_label.config(
                text=f"{decrease:.2f}% Decrease"
            )

    # --------------------------------------------------
    # Clear all fields
    # --------------------------------------------------

    def clear_fields(self):

        self.first_entry.delete(0, tk.END)
        self.second_entry.delete(0, tk.END)

        self.result_label.config(
            text="Enter values and click Calculate"
        )


# ------------------------------------------------------
# Start the application
# ------------------------------------------------------

if __name__ == "__main__":

    app = PercentageCalculator()
    app.mainloop()
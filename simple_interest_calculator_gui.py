import tkinter as tk
from tkinter import messagebox


class InterestCalculator(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window settings
        self.title("Interest Calculator")
        self.geometry("440x700")
        self.minsize(440, 700)
        self.configure(bg="#f3f3f3")

        # Create the GUI
        self._build_ui()

    def _build_ui(self):

        # -------------------------
        # Title
        # -------------------------

        title = tk.Label(
            self,
            text="Interest Calculator",
            font=("Segoe UI", 22, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )
        title.pack(pady=(25, 20))


        # -------------------------
        # Principal Amount
        # -------------------------

        principal_label = tk.Label(
            self,
            text="Principal Amount",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        principal_label.pack(pady=(5, 5))

        self.principal_entry = tk.Entry(
            self,
            font=("Segoe UI", 15),
            justify="center",
            bd=1
        )
        self.principal_entry.pack(
            padx=40,
            fill="x",
            ipady=8
        )


        # -------------------------
        # Rate of Interest
        # -------------------------

        rate_label = tk.Label(
            self,
            text="Rate of Interest (%)",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        rate_label.pack(pady=(18, 5))

        self.rate_entry = tk.Entry(
            self,
            font=("Segoe UI", 15),
            justify="center",
            bd=1
        )
        self.rate_entry.pack(
            padx=40,
            fill="x",
            ipady=8
        )


        # -------------------------
        # Time
        # -------------------------

        time_label = tk.Label(
            self,
            text="Time",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        time_label.pack(pady=(18, 5))

        self.time_entry = tk.Entry(
            self,
            font=("Segoe UI", 15),
            justify="center",
            bd=1
        )
        self.time_entry.pack(
            padx=40,
            fill="x",
            ipady=8
        )


        # -------------------------
        # Time Unit
        # -------------------------

        time_unit_label = tk.Label(
            self,
            text="Time Unit",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        time_unit_label.pack(pady=(18, 5))

        self.time_unit = tk.StringVar(value="Years")

        time_unit_menu = tk.OptionMenu(
            self,
            self.time_unit,
            "Years",
            "Months",
            "Days"
        )

        time_unit_menu.config(
            font=("Segoe UI", 12),
            bg="#ffffff",
            width=15,
            bd=1
        )

        time_unit_menu.pack()


        # -------------------------
        # Compound Frequency
        # -------------------------

        frequency_label = tk.Label(
            self,
            text="Compound Frequency",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        frequency_label.pack(pady=(18, 5))

        self.frequency = tk.StringVar(value="Yearly")

        frequency_menu = tk.OptionMenu(
            self,
            self.frequency,
            "Yearly",
            "Half-Yearly",
            "Quarterly",
            "Monthly"
        )

        frequency_menu.config(
            font=("Segoe UI", 12),
            bg="#ffffff",
            width=15,
            bd=1
        )

        frequency_menu.pack()


        # -------------------------
        # Buttons
        # -------------------------

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        button_frame.pack(pady=25)

        calculate_button = tk.Button(
            button_frame,
            text="Calculate",
            font=("Segoe UI", 13, "bold"),
            bg="#ff9f0a",
            fg="#ffffff",
            bd=0,
            padx=25,
            pady=10,
            command=self.calculate
        )
        calculate_button.grid(
            row=0,
            column=0,
            padx=8
        )

        clear_button = tk.Button(
            button_frame,
            text="Clear",
            font=("Segoe UI", 13, "bold"),
            bg="#d9d9d9",
            fg="#111111",
            bd=0,
            padx=30,
            pady=10,
            command=self.clear
        )
        clear_button.grid(
            row=0,
            column=1,
            padx=8
        )


        # -------------------------
        # Result Section
        # -------------------------

        result_frame = tk.Frame(
            self,
            bg="#ffffff",
            bd=1,
            relief="solid"
        )
        result_frame.pack(
            padx=40,
            fill="x",
            pady=(0, 20)
        )

        result_title = tk.Label(
            result_frame,
            text="Results",
            font=("Segoe UI", 15, "bold"),
            bg="#ffffff",
            fg="#111111"
        )
        result_title.pack(pady=(15, 10))

        self.simple_result = tk.Label(
            result_frame,
            text="Simple Interest: --",
            font=("Segoe UI", 13),
            bg="#ffffff",
            fg="#111111"
        )
        self.simple_result.pack(pady=5)

        self.compound_result = tk.Label(
            result_frame,
            text="Compound Interest: --",
            font=("Segoe UI", 13),
            bg="#ffffff",
            fg="#111111"
        )
        self.compound_result.pack(pady=5)

        self.amount_result = tk.Label(
            result_frame,
            text="Compound Amount: --",
            font=("Segoe UI", 13, "bold"),
            bg="#ffffff",
            fg="#111111"
        )
        self.amount_result.pack(pady=(5, 15))


    # -------------------------
    # Calculate Interest
    # -------------------------

    def calculate(self):

        try:
            # Get values from the input fields
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get())
            time = float(self.time_entry.get())

            # Validate the entered values
            if principal <= 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Principal amount must be greater than 0."
                )
                return

            if rate < 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Rate of interest cannot be negative."
                )
                return

            if time <= 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Time must be greater than 0."
                )
                return


            # -------------------------
            # Convert time into years
            # -------------------------

            selected_unit = self.time_unit.get()

            if selected_unit == "Months":
                time = time / 12

            elif selected_unit == "Days":
                time = time / 365


            # -------------------------
            # Simple Interest
            # -------------------------
            #
            # SI = (P × R × T) / 100
            #

            simple_interest = (
                principal * rate * time
            ) / 100


            # -------------------------
            # Compound Interest
            # -------------------------
            #
            # Amount = P × (1 + R/n)^(nT)
            #
            # CI = Amount - P
            #

            selected_frequency = self.frequency.get()

            if selected_frequency == "Yearly":
                n = 1

            elif selected_frequency == "Half-Yearly":
                n = 2

            elif selected_frequency == "Quarterly":
                n = 4

            else:
                n = 12


            # Convert percentage rate into decimal
            rate_decimal = rate / 100

            # Calculate compound amount
            compound_amount = principal * (
                1 + rate_decimal / n
            ) ** (n * time)

            # Calculate compound interest
            compound_interest = compound_amount - principal


            # -------------------------
            # Display Results
            # -------------------------

            self.simple_result.config(
                text=f"Simple Interest: {simple_interest:.2f}"
            )

            self.compound_result.config(
                text=f"Compound Interest: {compound_interest:.2f}"
            )

            self.amount_result.config(
                text=f"Compound Amount: {compound_amount:.2f}"
            )


        except ValueError:

            # This runs if the user enters
            # something that is not a valid number.

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers."
            )


    # -------------------------
    # Clear all fields
    # -------------------------

    def clear(self):

        self.principal_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)

        self.time_unit.set("Years")
        self.frequency.set("Yearly")

        self.simple_result.config(
            text="Simple Interest: --"
        )

        self.compound_result.config(
            text="Compound Interest: --"
        )

        self.amount_result.config(
            text="Compound Amount: --"
        )


# -------------------------
# Start the application
# -------------------------

if __name__ == "__main__":
    app = InterestCalculator()
    app.mainloop()
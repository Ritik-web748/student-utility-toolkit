import tkinter as tk
from tkinter import messagebox


class EMICalculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("EMI Calculator")
        self.geometry("500x650")
        self.configure(bg="#f3f3f3")

        self._build_ui()

    def _build_ui(self):

        tk.Label(
            self,
            text="EMI Calculator",
            font=("Segoe UI", 25, "bold"),
            bg="#f3f3f3"
        ).pack(pady=(25, 10))

        tk.Label(
            self,
            text="Calculate monthly loan payment",
            font=("Segoe UI", 11),
            bg="#f3f3f3",
            fg="#555555"
        ).pack(pady=(0, 20))

        self.create_input(
            "Loan Amount",
            "loan_entry"
        )

        self.create_input(
            "Annual Interest Rate (%)",
            "rate_entry"
        )

        tk.Label(
            self,
            text="Loan Duration",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3"
        ).pack(pady=(15, 5))

        duration_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        duration_frame.pack()

        self.duration_entry = tk.Entry(
            duration_frame,
            font=("Segoe UI", 13),
            justify="center",
            width=15
        )
        self.duration_entry.pack(
            side="left",
            ipady=7
        )

        self.duration_unit = tk.StringVar(
            value="Years"
        )

        tk.OptionMenu(
            duration_frame,
            self.duration_unit,
            "Years",
            "Months"
        ).pack(
            side="left",
            padx=10
        )

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        button_frame.pack(pady=25)

        tk.Button(
            button_frame,
            text="Calculate EMI",
            font=("Segoe UI", 13, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=25,
            pady=10,
            command=self.calculate
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            font=("Segoe UI", 13, "bold"),
            bg="#d9d9d9",
            fg="#111111",
            bd=0,
            padx=30,
            pady=10,
            command=self.clear
        ).grid(row=0, column=1, padx=5)

        self.result_label = tk.Label(
            self,
            text="EMI: --\n\nTotal Interest: --\n\nTotal Payment: --",
            font=("Segoe UI", 15, "bold"),
            bg="#ffffff",
            bd=1,
            relief="solid",
            padx=30,
            pady=25,
            justify="center"
        )
        self.result_label.pack(
            padx=40,
            fill="x"
        )

    def create_input(self, label_text, attribute_name):

        tk.Label(
            self,
            text=label_text,
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3"
        ).pack(pady=(10, 5))

        entry = tk.Entry(
            self,
            font=("Segoe UI", 14),
            justify="center"
        )

        entry.pack(
            padx=50,
            fill="x",
            ipady=8
        )

        setattr(
            self,
            attribute_name,
            entry
        )

    def calculate(self):

        try:

            principal = float(
                self.loan_entry.get()
            )

            annual_rate = float(
                self.rate_entry.get()
            )

            duration = float(
                self.duration_entry.get()
            )

            if principal <= 0:
                raise ValueError

            if annual_rate < 0:
                raise ValueError

            if duration <= 0:
                raise ValueError

            if self.duration_unit.get() == "Years":
                months = duration * 12
            else:
                months = duration

            months = int(months)

            monthly_rate = (
                annual_rate / 12 / 100
            )

            if monthly_rate == 0:

                emi = principal / months

            else:

                emi = (
                    principal
                    * monthly_rate
                    * (1 + monthly_rate) ** months
                    / (
                        (1 + monthly_rate) ** months - 1
                    )
                )

            total_payment = emi * months
            total_interest = total_payment - principal

            self.result_label.config(
                text=(
                    f"Monthly EMI: ₹{emi:,.2f}\n\n"
                    f"Total Interest: ₹{total_interest:,.2f}\n\n"
                    f"Total Payment: ₹{total_payment:,.2f}"
                )
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid positive numbers."
            )

    def clear(self):

        self.loan_entry.delete(
            0,
            tk.END
        )

        self.rate_entry.delete(
            0,
            tk.END
        )

        self.duration_entry.delete(
            0,
            tk.END
        )

        self.duration_unit.set(
            "Years"
        )

        self.result_label.config(
            text="EMI: --\n\nTotal Interest: --\n\nTotal Payment: --"
        )


if __name__ == "__main__":

    app = EMICalculator()
    app.mainloop()
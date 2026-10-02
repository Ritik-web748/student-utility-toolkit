import tkinter as tk
from tkinter import messagebox


class GPACalculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("GPA / CGPA Calculator")
        self.geometry("650x700")
        self.minsize(650, 700)
        self.configure(bg="#f3f3f3")

        self.subject_rows = []

        self._build_ui()

    def _build_ui(self):

        title = tk.Label(
            self,
            text="GPA / CGPA Calculator",
            font=("Segoe UI", 24, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )
        title.pack(pady=(20, 5))

        info = tk.Label(
            self,
            text="Enter subjects, credits and grades",
            font=("Segoe UI", 12),
            bg="#f3f3f3",
            fg="#555555"
        )
        info.pack(pady=(0, 15))

        table = tk.Frame(self, bg="#f3f3f3")
        table.pack(padx=25, fill="x")

        headers = ["Subject", "Credits", "Grade"]

        for column, header in enumerate(headers):
            tk.Label(
                table,
                text=header,
                font=("Segoe UI", 12, "bold"),
                bg="#d9d9d9",
                fg="#111111"
            ).grid(
                row=0,
                column=column,
                sticky="nsew",
                padx=2,
                pady=2,
                ipady=8
            )

        for i in range(6):
            self.add_subject_row(table, i + 1)

        button_frame = tk.Frame(self, bg="#f3f3f3")
        button_frame.pack(pady=20)

        tk.Button(
            button_frame,
            text="Calculate GPA",
            font=("Segoe UI", 12, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            command=self.calculate_gpa
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Calculate CGPA",
            font=("Segoe UI", 12, "bold"),
            bg="#555555",
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            command=self.calculate_cgpa
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Clear",
            font=("Segoe UI", 12, "bold"),
            bg="#d9d9d9",
            fg="#111111",
            bd=0,
            padx=30,
            pady=10,
            command=self.clear
        ).grid(row=0, column=2, padx=5)

        self.result_label = tk.Label(
            self,
            text="Result: --",
            font=("Segoe UI", 18, "bold"),
            bg="#ffffff",
            fg="#111111",
            bd=1,
            relief="solid",
            padx=30,
            pady=20
        )
        self.result_label.pack(
            padx=40,
            fill="x",
            pady=10
        )

        scale = tk.Label(
            self,
            text=(
                "Grade Points:\n"
                "A+ = 10    A = 9    B+ = 8    B = 7\n"
                "C+ = 6    C = 5    D = 4    F = 0"
            ),
            font=("Segoe UI", 10),
            bg="#f3f3f3",
            fg="#555555",
            justify="center"
        )
        scale.pack(pady=10)

    def add_subject_row(self, table, row):

        name_entry = tk.Entry(
            table,
            font=("Segoe UI", 12)
        )
        name_entry.grid(
            row=row,
            column=0,
            sticky="nsew",
            padx=2,
            pady=2,
            ipady=6
        )

        credit_entry = tk.Entry(
            table,
            font=("Segoe UI", 12),
            justify="center"
        )
        credit_entry.grid(
            row=row,
            column=1,
            sticky="nsew",
            padx=2,
            pady=2,
            ipady=6
        )

        grade_var = tk.StringVar(value="A")

        grade_menu = tk.OptionMenu(
            table,
            grade_var,
            "A+",
            "A",
            "B+",
            "B",
            "C+",
            "C",
            "D",
            "F"
        )
        grade_menu.config(
            font=("Segoe UI", 11),
            bg="white"
        )
        grade_menu.grid(
            row=row,
            column=2,
            sticky="nsew",
            padx=2,
            pady=2
        )

        self.subject_rows.append(
            (name_entry, credit_entry, grade_var)
        )

    def get_grade_point(self, grade):

        grade_points = {
            "A+": 10,
            "A": 9,
            "B+": 8,
            "B": 7,
            "C+": 6,
            "C": 5,
            "D": 4,
            "F": 0
        }

        return grade_points[grade]

    def calculate_gpa(self):

        total_points = 0
        total_credits = 0

        try:

            for name_entry, credit_entry, grade_var in self.subject_rows:

                credit_text = credit_entry.get().strip()

                if credit_text == "":
                    continue

                credits = float(credit_text)

                if credits <= 0:
                    raise ValueError

                grade = grade_var.get()
                grade_point = self.get_grade_point(grade)

                total_points += credits * grade_point
                total_credits += credits

            if total_credits == 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter at least one subject."
                )
                return

            gpa = total_points / total_credits

            self.result_label.config(
                text=f"GPA / SGPA: {gpa:.2f}"
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid credit values."
            )

    def calculate_cgpa(self):

        window = tk.Toplevel(self)
        window.title("CGPA Calculator")
        window.geometry("400x500")
        window.configure(bg="#f3f3f3")

        tk.Label(
            window,
            text="Enter Semester GPAs",
            font=("Segoe UI", 18, "bold"),
            bg="#f3f3f3"
        ).pack(pady=20)

        entries = []

        for i in range(8):

            frame = tk.Frame(window, bg="#f3f3f3")
            frame.pack(pady=5)

            tk.Label(
                frame,
                text=f"Semester {i + 1}",
                font=("Segoe UI", 11),
                bg="#f3f3f3"
            ).pack(side="left", padx=10)

            entry = tk.Entry(
                frame,
                font=("Segoe UI", 11),
                width=10
            )
            entry.pack(side="left")

            entries.append(entry)

        def calculate():

            try:

                values = []

                for entry in entries:

                    value = entry.get().strip()

                    if value:
                        gpa = float(value)

                        if gpa < 0 or gpa > 10:
                            raise ValueError

                        values.append(gpa)

                if not values:
                    raise ValueError

                cgpa = sum(values) / len(values)

                result.config(
                    text=f"CGPA: {cgpa:.2f}"
                )

            except ValueError:

                messagebox.showerror(
                    "Invalid Input",
                    "Enter valid GPA values between 0 and 10."
                )

        tk.Button(
            window,
            text="Calculate CGPA",
            font=("Segoe UI", 12, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            command=calculate
        ).pack(pady=20)

        result = tk.Label(
            window,
            text="CGPA: --",
            font=("Segoe UI", 18, "bold"),
            bg="#ffffff",
            padx=30,
            pady=15
        )
        result.pack()

    def clear(self):

        for name_entry, credit_entry, grade_var in self.subject_rows:

            name_entry.delete(0, tk.END)
            credit_entry.delete(0, tk.END)
            grade_var.set("A")

        self.result_label.config(
            text="Result: --"
        )


if __name__ == "__main__":

    app = GPACalculator()
    app.mainloop()

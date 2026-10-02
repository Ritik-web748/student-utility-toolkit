import tkinter as tk
from tkinter import messagebox


class GradeCalculator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Grade Calculator")
        self.geometry("750x650")
        self.minsize(650, 550)
        self.configure(bg="#f3f3f3")

        # Store all subject input fields
        self.subject_rows = []

        self.create_ui()

    # ==================================================
    # CREATE MAIN USER INTERFACE
    # ==================================================

    def create_ui(self):

        # -------------------------------
        # Title
        # -------------------------------

        title = tk.Label(
            self,
            text="Grade Calculator",
            font=("Segoe UI", 26, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        title.pack(pady=(20, 5))

        subtitle = tk.Label(
            self,
            text="Create your own subjects and enter their marks",
            font=("Segoe UI", 11),
            bg="#f3f3f3",
            fg="#555555"
        )

        subtitle.pack(pady=(0, 15))

        # -------------------------------
        # Number of subjects
        # -------------------------------

        number_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )

        number_frame.pack(pady=5)

        number_label = tk.Label(
            number_frame,
            text="Number of Subjects:",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3"
        )

        number_label.pack(side="left", padx=5)

        self.subject_count_entry = tk.Entry(
            number_frame,
            font=("Segoe UI", 12),
            width=8,
            justify="center"
        )

        self.subject_count_entry.pack(
            side="left",
            padx=5
        )

        create_button = tk.Button(
            number_frame,
            text="Create Subjects",
            font=("Segoe UI", 11, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=12,
            pady=7,
            command=self.create_subject_rows
        )

        create_button.pack(
            side="left",
            padx=5
        )

        # -------------------------------
        # Subject area
        # -------------------------------

        self.subject_area = tk.Frame(
            self,
            bg="#ffffff",
            bd=1,
            relief="solid"
        )

        self.subject_area.pack(
            padx=30,
            pady=15,
            fill="both",
            expand=True
        )

        # -------------------------------
        # Buttons
        # -------------------------------

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )

        button_frame.pack(pady=10)

        calculate_button = tk.Button(
            button_frame,
            text="Calculate Grade",
            font=("Segoe UI", 13, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=20,
            pady=10,
            command=self.calculate
        )

        calculate_button.pack(
            side="left",
            padx=5
        )

        clear_button = tk.Button(
            button_frame,
            text="Clear",
            font=("Segoe UI", 11),
            padx=20,
            pady=10,
            command=self.clear_all
        )

        clear_button.pack(
            side="left",
            padx=5
        )

        # -------------------------------
        # Result area
        # -------------------------------

        self.result_label = tk.Label(
            self,
            text="Create subjects and enter marks",
            font=("Segoe UI", 15, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        self.result_label.pack(
            pady=(5, 20)
        )

    # ==================================================
    # CREATE SUBJECT INPUT ROWS
    # ==================================================

    def create_subject_rows(self):

        # Remove old subject rows
        for widget in self.subject_area.winfo_children():
            widget.destroy()

        self.subject_rows.clear()

        # Get number of subjects
        try:
            number_of_subjects = int(
                self.subject_count_entry.get()
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number of subjects."
            )

            return

        # Validate number
        if number_of_subjects <= 0:

            messagebox.showerror(
                "Invalid Number",
                "Number of subjects must be greater than 0."
            )

            return

        if number_of_subjects > 20:

            messagebox.showerror(
                "Too Many Subjects",
                "Please enter 20 or fewer subjects."
            )

            return

        # -------------------------------
        # Column headings
        # -------------------------------

        headings = [
            "Subject Name",
            "Maximum Marks",
            "Obtained Marks"
        ]

        for column, heading in enumerate(headings):

            label = tk.Label(
                self.subject_area,
                text=heading,
                font=("Segoe UI", 11, "bold"),
                bg="#ffffff"
            )

            label.grid(
                row=0,
                column=column,
                padx=10,
                pady=10
            )

        # -------------------------------
        # Create rows
        # -------------------------------

        for row in range(number_of_subjects):

            # Subject name
            name_entry = tk.Entry(
                self.subject_area,
                font=("Segoe UI", 11),
                width=25
            )

            name_entry.grid(
                row=row + 1,
                column=0,
                padx=10,
                pady=5
            )

            # Maximum marks
            max_marks_entry = tk.Entry(
                self.subject_area,
                font=("Segoe UI", 11),
                width=15,
                justify="center"
            )

            max_marks_entry.grid(
                row=row + 1,
                column=1,
                padx=10,
                pady=5
            )

            # Obtained marks
            obtained_marks_entry = tk.Entry(
                self.subject_area,
                font=("Segoe UI", 11),
                width=15,
                justify="center"
            )

            obtained_marks_entry.grid(
                row=row + 1,
                column=2,
                padx=10,
                pady=5
            )

            # Store the three entries
            self.subject_rows.append(
                (
                    name_entry,
                    max_marks_entry,
                    obtained_marks_entry
                )
            )

    # ==================================================
    # CALCULATE GRADE
    # ==================================================

    def calculate(self):

        # Make sure subjects have been created
        if not self.subject_rows:

            messagebox.showerror(
                "No Subjects",
                "Please create the subjects first."
            )

            return

        total_max_marks = 0
        total_obtained_marks = 0

        # ----------------------------------------------
        # Read every subject
        # ----------------------------------------------

        for index, row in enumerate(self.subject_rows):

            name_entry = row[0]
            max_marks_entry = row[1]
            obtained_marks_entry = row[2]

            subject_name = name_entry.get().strip()

            # Check subject name
            if subject_name == "":

                messagebox.showerror(
                    "Missing Subject Name",
                    f"Please enter a name for Subject {index + 1}."
                )

                return

            # Get maximum marks
            try:

                max_marks = float(
                    max_marks_entry.get()
                )

            except ValueError:

                messagebox.showerror(
                    "Invalid Marks",
                    f"Enter valid maximum marks for {subject_name}."
                )

                return

            # Get obtained marks
            try:

                obtained_marks = float(
                    obtained_marks_entry.get()
                )

            except ValueError:

                messagebox.showerror(
                    "Invalid Marks",
                    f"Enter valid obtained marks for {subject_name}."
                )

                return

            # Maximum marks must be greater than zero
            if max_marks <= 0:

                messagebox.showerror(
                    "Invalid Maximum Marks",
                    f"Maximum marks for {subject_name} must be greater than 0."
                )

                return

            # Obtained marks cannot be negative
            if obtained_marks < 0:

                messagebox.showerror(
                    "Invalid Obtained Marks",
                    f"Obtained marks for {subject_name} cannot be negative."
                )

                return

            # Obtained marks cannot exceed maximum marks
            if obtained_marks > max_marks:

                messagebox.showerror(
                    "Invalid Marks",
                    f"Obtained marks for {subject_name} "
                    f"cannot be greater than {max_marks:g}."
                )

                return

            # Add marks to totals
            total_max_marks += max_marks
            total_obtained_marks += obtained_marks

        # ----------------------------------------------
        # Calculate percentage
        # ----------------------------------------------

        percentage = (
            total_obtained_marks
            / total_max_marks
        ) * 100

        # ----------------------------------------------
        # Calculate grade
        # ----------------------------------------------

        if percentage >= 90:
            grade = "A+"

        elif percentage >= 80:
            grade = "A"

        elif percentage >= 70:
            grade = "B"

        elif percentage >= 60:
            grade = "C"

        elif percentage >= 50:
            grade = "D"

        elif percentage >= 40:
            grade = "E"

        else:
            grade = "F"

        # ----------------------------------------------
        # Display result
        # ----------------------------------------------

        self.result_label.config(
            text=(
                f"Total: {total_obtained_marks:g} / "
                f"{total_max_marks:g}    |    "
                f"Percentage: {percentage:.2f}%    |    "
                f"Grade: {grade}"
            )
        )

    # ==================================================
    # CLEAR EVERYTHING
    # ==================================================

    def clear_all(self):

        self.subject_count_entry.delete(
            0,
            tk.END
        )

        for widget in self.subject_area.winfo_children():
            widget.destroy()

        self.subject_rows.clear()

        self.result_label.config(
            text="Create subjects and enter marks"
        )


# ======================================================
# START APPLICATION
# ======================================================

if __name__ == "__main__":

    app = GradeCalculator()

    app.mainloop()
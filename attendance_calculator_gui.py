import tkinter as tk
from tkinter import messagebox


class AttendanceCalculator(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window settings
        self.title("Student Attendance Calculator")
        self.geometry("440x650")
        self.minsize(440, 650)
        self.configure(bg="#f3f3f3")

        # Create the GUI
        self._build_ui()

    def _build_ui(self):

        # -------------------------
        # Title
        # -------------------------

        title = tk.Label(
            self,
            text="Student Attendance Calculator",
            font=("Segoe UI", 21, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )
        title.pack(pady=(25, 20))


        # -------------------------
        # Total Lectures
        # -------------------------

        total_label = tk.Label(
            self,
            text="Total Lectures",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        total_label.pack(pady=(5, 5))

        self.total_entry = tk.Entry(
            self,
            font=("Segoe UI", 15),
            justify="center",
            bd=1
        )
        self.total_entry.pack(
            padx=40,
            fill="x",
            ipady=8
        )


        # -------------------------
        # Attended Lectures
        # -------------------------

        attended_label = tk.Label(
            self,
            text="Attended Lectures",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        attended_label.pack(pady=(18, 5))

        self.attended_entry = tk.Entry(
            self,
            font=("Segoe UI", 15),
            justify="center",
            bd=1
        )
        self.attended_entry.pack(
            padx=40,
            fill="x",
            ipady=8
        )


        # -------------------------
        # Target Attendance
        # -------------------------

        target_label = tk.Label(
            self,
            text="Target Attendance (%)",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        target_label.pack(pady=(18, 5))

        self.target_entry = tk.Entry(
            self,
            font=("Segoe UI", 15),
            justify="center",
            bd=1
        )
        self.target_entry.insert(0, "75")
        self.target_entry.pack(
            padx=40,
            fill="x",
            ipady=8
        )


        # -------------------------
        # Calculate Button
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
            text="Attendance Result",
            font=("Segoe UI", 15, "bold"),
            bg="#ffffff",
            fg="#111111"
        )
        result_title.pack(pady=(15, 10))

        self.percentage_result = tk.Label(
            result_frame,
            text="Attendance: --",
            font=("Segoe UI", 14, "bold"),
            bg="#ffffff",
            fg="#111111"
        )
        self.percentage_result.pack(pady=5)

        self.status_result = tk.Label(
            result_frame,
            text="Status: --",
            font=("Segoe UI", 13),
            bg="#ffffff",
            fg="#111111"
        )
        self.status_result.pack(pady=5)

        self.action_result = tk.Label(
            result_frame,
            text="Recommendation: --",
            font=("Segoe UI", 11),
            bg="#ffffff",
            fg="#111111",
            wraplength=330,
            justify="center"
        )
        self.action_result.pack(pady=(5, 15))


    # -------------------------
    # Calculate Attendance
    # -------------------------

    def calculate(self):

        try:
            # Get values entered by the user
            total_lectures = int(self.total_entry.get())
            attended_lectures = int(self.attended_entry.get())
            target_attendance = float(self.target_entry.get())

            # -------------------------
            # Validate Input
            # -------------------------

            if total_lectures <= 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Total lectures must be greater than 0."
                )
                return

            if attended_lectures < 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Attended lectures cannot be negative."
                )
                return

            if attended_lectures > total_lectures:
                messagebox.showerror(
                    "Invalid Input",
                    "Attended lectures cannot be greater than total lectures."
                )
                return

            if target_attendance <= 0 or target_attendance > 100:
                messagebox.showerror(
                    "Invalid Input",
                    "Target attendance must be between 0 and 100."
                )
                return


            # -------------------------
            # Attendance Percentage
            # -------------------------

            attendance = (
                attended_lectures / total_lectures
            ) * 100


            # -------------------------
            # Check Target
            # -------------------------

            if attendance >= target_attendance:

                status = "Target Achieved"

                # Calculate how many lectures can be missed
                # before attendance falls below the target.

                current_missed = total_lectures - attended_lectures

                if target_attendance < 100:
                    max_total = int(
                        attended_lectures * 100 / target_attendance
                    )

                    can_miss = max_total - total_lectures

                    if can_miss > 0:
                        recommendation = (
                            f"You can miss approximately "
                            f"{can_miss} more lecture(s) "
                            f"while staying around the target."
                        )
                    else:
                        recommendation = (
                            "You are currently at the target. "
                            "Keep attending lectures."
                        )

                else:
                    recommendation = (
                        "To maintain 100% attendance, "
                        "you need to attend every lecture."
                    )

            else:

                status = "Target Not Achieved"

                # Calculate how many consecutive lectures
                # need to be attended to reach the target.

                required_lectures = 0
                future_total = total_lectures
                future_attended = attended_lectures

                while (
                    future_attended / future_total
                ) * 100 < target_attendance:

                    future_attended += 1
                    future_total += 1
                    required_lectures += 1

                recommendation = (
                    f"You need to attend the next "
                    f"{required_lectures} lecture(s) "
                    f"to reach approximately {target_attendance:.1f}%."
                )


            # -------------------------
            # Display Results
            # -------------------------

            self.percentage_result.config(
                text=f"Attendance: {attendance:.2f}%"
            )

            self.status_result.config(
                text=f"Status: {status}"
            )

            self.action_result.config(
                text=f"Recommendation: {recommendation}"
            )


        except ValueError:

            # Runs when the user enters
            # something that is not a valid number.

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers."
            )


    # -------------------------
    # Clear all fields
    # -------------------------

    def clear(self):

        self.total_entry.delete(0, tk.END)
        self.attended_entry.delete(0, tk.END)

        self.target_entry.delete(0, tk.END)
        self.target_entry.insert(0, "75")

        self.percentage_result.config(
            text="Attendance: --"
        )

        self.status_result.config(
            text="Status: --"
        )

        self.action_result.config(
            text="Recommendation: --"
        )


# -------------------------
# Start the application
# -------------------------

if __name__ == "__main__":
    app = AttendanceCalculator()
    app.mainloop()
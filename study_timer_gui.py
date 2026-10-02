import tkinter as tk
from tkinter import messagebox


class StudyTimer(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Study Timer")
        self.geometry("450x550")
        self.configure(bg="#f3f3f3")

        self.remaining_seconds = 25 * 60
        self.timer_running = False
        self.study_mode = True

        self._build_ui()

    def _build_ui(self):

        tk.Label(
            self,
            text="Study Timer",
            font=("Segoe UI", 26, "bold"),
            bg="#f3f3f3"
        ).pack(pady=(30, 10))

        self.mode_label = tk.Label(
            self,
            text="Study Session",
            font=("Segoe UI", 16, "bold"),
            bg="#f3f3f3"
        )
        self.mode_label.pack(pady=10)

        self.timer_label = tk.Label(
            self,
            text="25:00",
            font=("Segoe UI", 55, "bold"),
            bg="#ffffff",
            fg="#111111",
            bd=1,
            relief="solid",
            padx=30,
            pady=20
        )
        self.timer_label.pack(pady=30)

        tk.Label(
            self,
            text="Study: 25 minutes    Break: 5 minutes",
            font=("Segoe UI", 11),
            bg="#f3f3f3",
            fg="#555555"
        ).pack()

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        button_frame.pack(pady=30)

        tk.Button(
            button_frame,
            text="Start",
            font=("Segoe UI", 13, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=25,
            pady=10,
            command=self.start_timer
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Pause",
            font=("Segoe UI", 13, "bold"),
            bg="#555555",
            fg="white",
            bd=0,
            padx=25,
            pady=10,
            command=self.pause_timer
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Reset",
            font=("Segoe UI", 13, "bold"),
            bg="#d9d9d9",
            fg="#111111",
            bd=0,
            padx=25,
            pady=10,
            command=self.reset_timer
        ).grid(row=0, column=2, padx=5)

    def start_timer(self):

        if not self.timer_running:

            self.timer_running = True
            self.update_timer()

    def pause_timer(self):

        self.timer_running = False

    def reset_timer(self):

        self.timer_running = False
        self.study_mode = True
        self.remaining_seconds = 25 * 60

        self.mode_label.config(
            text="Study Session"
        )

        self.update_display()

    def update_timer(self):

        if not self.timer_running:
            return

        if self.remaining_seconds > 0:

            self.remaining_seconds -= 1
            self.update_display()

            self.after(
                1000,
                self.update_timer
            )

        else:

            self.timer_running = False

            if self.study_mode:

                self.study_mode = False
                self.remaining_seconds = 5 * 60

                self.mode_label.config(
                    text="Break Time"
                )

                messagebox.showinfo(
                    "Study Session Complete",
                    "Study session completed. Take a short break."
                )

            else:

                self.study_mode = True
                self.remaining_seconds = 25 * 60

                self.mode_label.config(
                    text="Study Session"
                )

                messagebox.showinfo(
                    "Break Complete",
                    "Break completed. Time to study."
                )

            self.update_display()

    def update_display(self):

        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60

        self.timer_label.config(
            text=f"{minutes:02d}:{seconds:02d}"
        )


if __name__ == "__main__":

    app = StudyTimer()
    app.mainloop()
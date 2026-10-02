import tkinter as tk
from tkinter import messagebox
import string
import secrets


class PasswordGenerator(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Password Generator")
        self.geometry("500x550")
        self.configure(bg="#f3f3f3")

        self._build_ui()

    def _build_ui(self):

        tk.Label(
            self,
            text="Password Generator",
            font=("Segoe UI", 25, "bold"),
            bg="#f3f3f3"
        ).pack(pady=(30, 10))

        tk.Label(
            self,
            text="Generate a random password",
            font=("Segoe UI", 11),
            bg="#f3f3f3",
            fg="#555555"
        ).pack(pady=(0, 25))

        tk.Label(
            self,
            text="Password Length",
            font=("Segoe UI", 13, "bold"),
            bg="#f3f3f3"
        ).pack()

        self.length_entry = tk.Entry(
            self,
            font=("Segoe UI", 14),
            justify="center"
        )
        self.length_entry.insert(
            0,
            "16"
        )
        self.length_entry.pack(
            padx=80,
            fill="x",
            ipady=8,
            pady=8
        )

        self.use_letters = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(
            self,
            text="Include Letters",
            variable=self.use_letters,
            font=("Segoe UI", 11),
            bg="#f3f3f3"
        ).pack()

        tk.Checkbutton(
            self,
            text="Include Numbers",
            variable=self.use_numbers,
            font=("Segoe UI", 11),
            bg="#f3f3f3"
        ).pack()

        tk.Checkbutton(
            self,
            text="Include Symbols",
            variable=self.use_symbols,
            font=("Segoe UI", 11),
            bg="#f3f3f3"
        ).pack()

        tk.Button(
            self,
            text="Generate Password",
            font=("Segoe UI", 13, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=25,
            pady=10,
            command=self.generate_password
        ).pack(pady=25)

        self.password_entry = tk.Entry(
            self,
            font=("Segoe UI", 14),
            justify="center",
            bd=1
        )
        self.password_entry.pack(
            padx=40,
            fill="x",
            ipady=10
        )

        tk.Button(
            self,
            text="Clear",
            font=("Segoe UI", 12, "bold"),
            bg="#d9d9d9",
            fg="#111111",
            bd=0,
            padx=30,
            pady=10,
            command=self.clear
        ).pack(pady=20)

    def generate_password(self):

        try:

            length = int(
                self.length_entry.get()
            )

            if length < 4 or length > 128:

                messagebox.showerror(
                    "Invalid Length",
                    "Password length must be between 4 and 128."
                )

                return

            character_pool = ""

            if self.use_letters.get():
                character_pool += string.ascii_letters

            if self.use_numbers.get():
                character_pool += string.digits

            if self.use_symbols.get():
                character_pool += string.punctuation

            if not character_pool:

                messagebox.showerror(
                    "No Characters Selected",
                    "Select at least one character type."
                )

                return

            password = "".join(
                secrets.choice(character_pool)
                for _ in range(length)
            )

            self.password_entry.delete(
                0,
                tk.END
            )

            self.password_entry.insert(
                0,
                password
            )

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid password length."
            )

    def clear(self):

        self.password_entry.delete(
            0,
            tk.END
        )


if __name__ == "__main__":

    app = PasswordGenerator()
    app.mainloop()
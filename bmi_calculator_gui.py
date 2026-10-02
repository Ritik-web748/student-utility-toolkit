import tkinter as tk
from tkinter import messagebox


class BMICalculator(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window settings
        self.title("BMI Calculator")
        self.geometry("460x700")
        self.minsize(460, 700)
        self.configure(bg="#f3f3f3")

        # Create the GUI
        self._build_ui()


    def _build_ui(self):

        # -------------------------
        # Title
        # -------------------------

        title = tk.Label(
            self,
            text="BMI Calculator",
            font=("Segoe UI", 24, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )
        title.pack(pady=(25, 10))


        # -------------------------
        # Information
        # -------------------------

        info = tk.Label(
            self,
            text="Enter height and weight to calculate BMI",
            font=("Segoe UI", 12),
            bg="#f3f3f3",
            fg="#555555"
        )
        info.pack(pady=(0, 20))


        # -------------------------
        # Height Unit
        # -------------------------

        height_unit_label = tk.Label(
            self,
            text="Height Unit",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        height_unit_label.pack(pady=(5, 5))


        self.height_unit = tk.StringVar(
            value="Centimetres"
        )


        height_unit_menu = tk.OptionMenu(
            self,
            self.height_unit,
            "Centimetres",
            "Metres",
            "Feet + Inches",
            command=self.change_height_unit
        )


        height_unit_menu.config(
            font=("Segoe UI", 12),
            bg="#ffffff",
            width=15,
            bd=1
        )


        height_unit_menu.pack()


        # -------------------------
        # Height Input Frame
        # -------------------------

        self.height_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        self.height_frame.pack(
            padx=40,
            fill="x",
            pady=(15, 0)
        )


        # Default height input
        self.height_entry = tk.Entry(
            self.height_frame,
            font=("Segoe UI", 15),
            justify="center",
            bd=1
        )


        self.height_entry.pack(
            fill="x",
            ipady=8
        )


        # Feet + Inches inputs
        self.feet_entry = None
        self.inches_entry = None


        # -------------------------
        # Weight Unit
        # -------------------------

        weight_unit_label = tk.Label(
            self,
            text="Weight Unit",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        weight_unit_label.pack(
            pady=(20, 5)
        )


        self.weight_unit = tk.StringVar(
            value="Kilograms"
        )


        weight_unit_menu = tk.OptionMenu(
            self,
            self.weight_unit,
            "Kilograms",
            "Pounds"
        )


        weight_unit_menu.config(
            font=("Segoe UI", 12),
            bg="#ffffff",
            width=15,
            bd=1
        )


        weight_unit_menu.pack()


        # -------------------------
        # Weight Input
        # -------------------------

        weight_label = tk.Label(
            self,
            text="Weight",
            font=("Segoe UI", 13),
            bg="#f3f3f3",
            fg="#111111"
        )
        weight_label.pack(
            pady=(18, 5)
        )


        self.weight_entry = tk.Entry(
            self,
            font=("Segoe UI", 15),
            justify="center",
            bd=1
        )


        self.weight_entry.pack(
            padx=40,
            fill="x",
            ipady=8
        )


        # -------------------------
        # Buttons
        # -------------------------

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        button_frame.pack(
            pady=25
        )


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
            pady=(0, 15)
        )


        result_title = tk.Label(
            result_frame,
            text="Result",
            font=("Segoe UI", 15, "bold"),
            bg="#ffffff",
            fg="#111111"
        )


        result_title.pack(
            pady=(15, 10)
        )


        self.result_label = tk.Label(
            result_frame,
            text="BMI: --",
            font=("Segoe UI", 18, "bold"),
            bg="#ffffff",
            fg="#111111"
        )


        self.result_label.pack(
            pady=(5, 10)
        )


        # -------------------------
        # Interpretation Note
        # -------------------------

        self.note_label = tk.Label(
            result_frame,
            text=(
                "BMI is a screening measure and does not measure "
                "fitness or overall health. For people under 18, "
                "BMI should be interpreted using age- and sex-specific "
                "growth references by a qualified health professional."
            ),
            font=("Segoe UI", 10),
            bg="#ffffff",
            fg="#555555",
            wraplength=350,
            justify="center"
        )


        self.note_label.pack(
            padx=15,
            pady=(5, 15)
        )


    # -------------------------
    # Change Height Unit
    # -------------------------

    def change_height_unit(self, selected_unit):

        # Remove existing height inputs
        for widget in self.height_frame.winfo_children():
            widget.destroy()


        # -------------------------
        # Centimetres / Metres
        # -------------------------

        if selected_unit in ["Centimetres", "Metres"]:

            self.height_entry = tk.Entry(
                self.height_frame,
                font=("Segoe UI", 15),
                justify="center",
                bd=1
            )


            self.height_entry.pack(
                fill="x",
                ipady=8
            )


            self.feet_entry = None
            self.inches_entry = None


        # -------------------------
        # Feet + Inches
        # -------------------------

        elif selected_unit == "Feet + Inches":

            feet_frame = tk.Frame(
                self.height_frame,
                bg="#f3f3f3"
            )


            feet_frame.pack(
                fill="x"
            )


            self.feet_entry = tk.Entry(
                feet_frame,
                font=("Segoe UI", 15),
                justify="center",
                bd=1
            )


            self.feet_entry.pack(
                side="left",
                expand=True,
                fill="x",
                ipady=8,
                padx=(0, 5)
            )


            feet_label = tk.Label(
                feet_frame,
                text="ft",
                font=("Segoe UI", 12),
                bg="#f3f3f3"
            )


            feet_label.pack(
                side="left",
                padx=5
            )


            self.inches_entry = tk.Entry(
                feet_frame,
                font=("Segoe UI", 15),
                justify="center",
                bd=1
            )


            self.inches_entry.pack(
                side="left",
                expand=True,
                fill="x",
                ipady=8,
                padx=(5, 0)
            )


            inches_label = tk.Label(
                feet_frame,
                text="in",
                font=("Segoe UI", 12),
                bg="#f3f3f3"
            )


            inches_label.pack(
                side="left",
                padx=5
            )


            self.height_entry = None


    # -------------------------
    # Calculate BMI
    # -------------------------

    def calculate(self):

        try:

            # -------------------------
            # Get Weight
            # -------------------------

            weight = float(
                self.weight_entry.get()
            )


            if weight <= 0:

                messagebox.showerror(
                    "Invalid Input",
                    "Weight must be greater than 0."
                )

                return


            # -------------------------
            # Convert Weight to KG
            # -------------------------

            if self.weight_unit.get() == "Pounds":

                weight = weight * 0.45359237


            # -------------------------
            # Get Height
            # -------------------------

            selected_unit = self.height_unit.get()


            # Centimetres
            if selected_unit == "Centimetres":

                height = float(
                    self.height_entry.get()
                )

                if height <= 0:

                    messagebox.showerror(
                        "Invalid Input",
                        "Height must be greater than 0."
                    )

                    return

                height = height / 100


            # Metres
            elif selected_unit == "Metres":

                height = float(
                    self.height_entry.get()
                )

                if height <= 0:

                    messagebox.showerror(
                        "Invalid Input",
                        "Height must be greater than 0."
                    )

                    return


            # Feet + Inches
            else:

                feet = float(
                    self.feet_entry.get()
                )

                inches = float(
                    self.inches_entry.get()
                )


                if feet < 0 or inches < 0:

                    messagebox.showerror(
                        "Invalid Input",
                        "Height values cannot be negative."
                    )

                    return


                if inches >= 12:

                    messagebox.showerror(
                        "Invalid Input",
                        "Inches must be less than 12."
                    )

                    return


                # Convert feet and inches to metres
                total_inches = (
                    feet * 12
                ) + inches


                height = (
                    total_inches * 0.0254
                )


                if height <= 0:

                    messagebox.showerror(
                        "Invalid Input",
                        "Height must be greater than 0."
                    )

                    return


            # -------------------------
            # BMI Formula
            # -------------------------
            #
            # BMI = Weight / Height²
            #

            bmi = weight / (
                height ** 2
            )


            # Display the calculated BMI
            self.result_label.config(
                text=f"BMI: {bmi:.2f}"
            )


        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numbers."
            )


    # -------------------------
    # Clear Everything
    # -------------------------

    def clear(self):

        # Clear weight
        self.weight_entry.delete(
            0,
            tk.END
        )


        # Reset height unit
        self.height_unit.set(
            "Centimetres"
        )


        # Recreate the default height input
        self.change_height_unit(
            "Centimetres"
        )


        # Clear height
        self.height_entry.delete(
            0,
            tk.END
        )


        # Reset weight unit
        self.weight_unit.set(
            "Kilograms"
        )


        # Reset result
        self.result_label.config(
            text="BMI: --"
        )


# -------------------------
# Start the application
# -------------------------

if __name__ == "__main__":

    app = BMICalculator()

    app.mainloop()
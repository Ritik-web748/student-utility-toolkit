import tkinter as tk
from tkinter import messagebox


class UnitConverter(tk.Tk):

    def __init__(self):
        super().__init__()

        # ==========================================
        # WINDOW SETTINGS
        # ==========================================

        self.title("Unit Converter")
        self.geometry("450x650")
        self.minsize(450, 650)
        self.configure(bg="#f3f3f3")

        # ==========================================
        # UNIT CONVERSION DATA
        #
        # Every normal unit is converted to a
        # common base unit first.
        #
        # Example:
        # km -> metre -> foot
        # ==========================================

        self.units = {

            # ======================================
            # LENGTH
            # Base unit: metre
            # ======================================

            "Length": {
                "Metre": 1,
                "Kilometre": 1000,
                "Centimetre": 0.01,
                "Millimetre": 0.001,
                "Micrometre": 0.000001,
                "Nanometre": 0.000000001,
                "Inch": 0.0254,
                "Foot": 0.3048,
                "Yard": 0.9144,
                "Mile": 1609.344,
                "Nautical Mile": 1852
            },

            # ======================================
            # MASS
            # Base unit: kilogram
            # ======================================

            "Mass": {
                "Kilogram": 1,
                "Gram": 0.001,
                "Milligram": 0.000001,
                "Microgram": 0.000000001,
                "Tonne": 1000,
                "Pound": 0.45359237,
                "Ounce": 0.028349523125
            },

            # ======================================
            # TIME
            # Base unit: second
            # ======================================

            "Time": {
                "Second": 1,
                "Millisecond": 0.001,
                "Microsecond": 0.000001,
                "Nanosecond": 0.000000001,
                "Minute": 60,
                "Hour": 3600,
                "Day": 86400,
                "Week": 604800
            },

            # ======================================
            # AREA
            # Base unit: square metre
            # ======================================

            "Area": {
                "Square Metre": 1,
                "Square Kilometre": 1000000,
                "Square Centimetre": 0.0001,
                "Square Millimetre": 0.000001,
                "Square Inch": 0.00064516,
                "Square Foot": 0.09290304,
                "Square Yard": 0.83612736,
                "Acre": 4046.8564224,
                "Hectare": 10000
            },

            # ======================================
            # VOLUME
            # Base unit: cubic metre
            # ======================================

            "Volume": {
                "Cubic Metre": 1,
                "Cubic Centimetre": 0.000001,
                "Cubic Millimetre": 0.000000001,
                "Litre": 0.001,
                "Millilitre": 0.000001,
                "Cubic Foot": 0.028316846592,
                "Cubic Inch": 0.000016387064,
                "Gallon (US)": 0.003785411784
            },

            # ======================================
            # SPEED
            # Base unit: metre per second
            # ======================================

            "Speed": {
                "Metre/Second": 1,
                "Kilometre/Hour": 1 / 3.6,
                "Centimetre/Second": 0.01,
                "Foot/Second": 0.3048,
                "Mile/Hour": 0.44704,
                "Knot": 0.5144444444
            },

            # ======================================
            # ACCELERATION
            # Base unit: metre per second squared
            # ======================================

            "Acceleration": {
                "Metre/Second²": 1,
                "Centimetre/Second²": 0.01,
                "Foot/Second²": 0.3048,
                "Standard Gravity": 9.80665
            },

            # ======================================
            # FORCE
            # Base unit: Newton
            # ======================================

            "Force": {
                "Newton": 1,
                "Kilonewton": 1000,
                "Meganewton": 1000000,
                "Dyne": 0.00001,
                "Pound-force": 4.4482216152605
            },

            # ======================================
            # PRESSURE
            # Base unit: Pascal
            # ======================================

            "Pressure": {
                "Pascal": 1,
                "Kilopascal": 1000,
                "Megapascal": 1000000,
                "Gigapascal": 1000000000,
                "Bar": 100000,
                "Millibar": 100,
                "Atmosphere": 101325,
                "PSI": 6894.757293168,
                "mmHg": 133.322387415
            },

            # ======================================
            # ENERGY
            # Base unit: Joule
            # ======================================

            "Energy": {
                "Joule": 1,
                "Kilojoule": 1000,
                "Megajoule": 1000000,
                "Erg": 0.0000001,
                "Calorie": 4.184,
                "Kilocalorie": 4184,
                "Watt-hour": 3600,
                "Kilowatt-hour": 3600000,
                "Foot-pound": 1.3558179483314
            },

            # ======================================
            # POWER
            # Base unit: Watt
            # ======================================

            "Power": {
                "Watt": 1,
                "Kilowatt": 1000,
                "Megawatt": 1000000,
                "Gigawatt": 1000000000,
                "Horsepower": 745.6998715823,
                "Foot-pound/Second": 1.3558179483314
            },

            # ======================================
            # FREQUENCY
            # Base unit: Hertz
            # ======================================

            "Frequency": {
                "Hertz": 1,
                "Kilohertz": 1000,
                "Megahertz": 1000000,
                "Gigahertz": 1000000000
            },

            # ======================================
            # DENSITY
            # Base unit: kg/m³
            # ======================================

            "Density": {
                "Kilogram/m³": 1,
                "Gram/cm³": 1000,
                "Gram/Litre": 1,
                "Pound/ft³": 16.01846337
            },

            # ======================================
            # MOMENTUM
            # Base unit: kg·m/s
            # ======================================

            "Momentum": {
                "kg·m/s": 1,
                "g·cm/s": 0.00001,
                "Pound·ft/s": 0.138254954376
            },

            # ======================================
            # TORQUE
            # Base unit: Newton metre
            # ======================================

            "Torque": {
                "Newton·metre": 1,
                "Kilonewton·metre": 1000,
                "Dyne·cm": 0.0000001,
                "Pound·foot": 1.3558179483314,
                "Pound·inch": 0.112984829027
            },

            # ======================================
            # DYNAMIC VISCOSITY
            # Base unit: Pascal second
            # ======================================

            "Dynamic Viscosity": {
                "Pascal·second": 1,
                "Millipascal·second": 0.001,
                "Poise": 0.1,
                "Centipoise": 0.001
            },

            # ======================================
            # KINEMATIC VISCOSITY
            # Base unit: m²/s
            # ======================================

            "Kinematic Viscosity": {
                "m²/s": 1,
                "cm²/s": 0.0001,
                "Stoke": 0.0001,
                "Centistoke": 0.000001
            },

            # ======================================
            # ANGLE
            # Base unit: radian
            # ======================================

            "Angle": {
                "Radian": 1,
                "Degree": 0.017453292519943,
                "Arcminute": 0.0002908882086657,
                "Arcsecond": 0.0000048481368111
            },

            # ======================================
            # ELECTRIC CURRENT
            # Base unit: Ampere
            # ======================================

            "Electric Current": {
                "Ampere": 1,
                "Milliampere": 0.001,
                "Microampere": 0.000001,
                "Kiloampere": 1000
            },

            # ======================================
            # VOLTAGE
            # Base unit: Volt
            # ======================================

            "Voltage": {
                "Volt": 1,
                "Millivolt": 0.001,
                "Kilovolt": 1000,
                "Megavolt": 1000000
            },

            # ======================================
            # RESISTANCE
            # Base unit: Ohm
            # ======================================

            "Resistance": {
                "Ohm": 1,
                "Milliohm": 0.001,
                "Kiloohm": 1000,
                "Megaohm": 1000000
            },

            # ======================================
            # ELECTRIC CHARGE
            # Base unit: Coulomb
            # ======================================

            "Electric Charge": {
                "Coulomb": 1,
                "Millicoulomb": 0.001,
                "Microcoulomb": 0.000001,
                "Nanocoulomb": 0.000000001
            },

            # ======================================
            # CAPACITANCE
            # Base unit: Farad
            # ======================================

            "Capacitance": {
                "Farad": 1,
                "Millifarad": 0.001,
                "Microfarad": 0.000001,
                "Nanofarad": 0.000000001,
                "Picofarad": 0.000000000001
            },

            # ======================================
            # INDUCTANCE
            # Base unit: Henry
            # ======================================

            "Inductance": {
                "Henry": 1,
                "Millihenry": 0.001,
                "Microhenry": 0.000001,
                "Nanohenry": 0.000000001
            },

            # ======================================
            # MAGNETIC FLUX
            # Base unit: Weber
            # ======================================

            "Magnetic Flux": {
                "Weber": 1,
                "Milliweber": 0.001,
                "Microweber": 0.000001,
                "Maxwell": 0.0000001
            },

            # ======================================
            # MAGNETIC FLUX DENSITY
            # Base unit: Tesla
            # ======================================

            "Magnetic Flux Density": {
                "Tesla": 1,
                "Millitesla": 0.001,
                "Microtesla": 0.000001,
                "Gauss": 0.0001
            },

            # ======================================
            # LUMINOUS INTENSITY
            # Base unit: Candela
            # ======================================

            "Luminous Intensity": {
                "Candela": 1
            },

            # ======================================
            # ILLUMINANCE
            # Base unit: Lux
            # ======================================

            "Illuminance": {
                "Lux": 1,
                "Phot": 10000
            },

            # ======================================
            # AMOUNT OF SUBSTANCE
            # Base unit: Mole
            # ======================================

            "Amount of Substance": {
                "Mole": 1,
                "Millimole": 0.001,
                "Micromole": 0.000001
            },

            # ======================================
            # DATA
            # Binary multiples are used here:
            # 1 KiB = 1024 bytes
            # ======================================

            "Data": {
                "Bit": 0.125,
                "Byte": 1,
                "Kilobyte": 1024,
                "Megabyte": 1024 ** 2,
                "Gigabyte": 1024 ** 3,
                "Terabyte": 1024 ** 4
            }
        }

        # ==========================================
        # CREATE GUI
        # ==========================================

        self.create_ui()

    # ==========================================
    # CREATE USER INTERFACE
    # ==========================================

    def create_ui(self):

        # ==========================================
        # TITLE
        # ==========================================

        title = tk.Label(
            self,
            text="Unit Converter",
            font=("Segoe UI", 24, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        title.pack(pady=(25, 5))

        subtitle = tk.Label(
            self,
            text="SI, MKS, FPS and common scientific units",
            font=("Segoe UI", 10),
            bg="#f3f3f3",
            fg="#666666"
        )

        subtitle.pack(pady=(0, 18))

        # ==========================================
        # CATEGORY
        # ==========================================

        category_label = tk.Label(
            self,
            text="Category",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        category_label.pack(pady=(3, 7))

        self.category_var = tk.StringVar(
            value="Length"
        )

        category_menu = tk.OptionMenu(
            self,
            self.category_var,
            *self.units.keys(),
            command=self.update_units
        )

        category_menu.config(
            font=("Segoe UI", 10),
            bg="white",
            fg="#111111",
            activebackground="#e6e6e6",
            activeforeground="#111111",
            bd=0,
            highlightthickness=0,
            width=25,
            pady=7
        )

        category_menu["menu"].config(
            font=("Segoe UI", 10),
            bg="white",
            fg="#111111"
        )

        category_menu.pack()

        # ==========================================
        # FROM UNIT
        # ==========================================

        from_label = tk.Label(
            self,
            text="From",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        from_label.pack(pady=(15, 7))

        self.from_var = tk.StringVar(
            value="Metre"
        )

        self.from_menu = tk.OptionMenu(
            self,
            self.from_var,
            "Metre"
        )

        self.from_menu.config(
            font=("Segoe UI", 10),
            bg="white",
            fg="#111111",
            activebackground="#e6e6e6",
            activeforeground="#111111",
            bd=0,
            highlightthickness=0,
            width=25,
            pady=7
        )

        self.from_menu.pack()

        # ==========================================
        # TO UNIT
        # ==========================================

        to_label = tk.Label(
            self,
            text="To",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        to_label.pack(pady=(15, 7))

        self.to_var = tk.StringVar(
            value="Kilometre"
        )

        self.to_menu = tk.OptionMenu(
            self,
            self.to_var,
            "Kilometre"
        )

        self.to_menu.config(
            font=("Segoe UI", 10),
            bg="white",
            fg="#111111",
            activebackground="#e6e6e6",
            activeforeground="#111111",
            bd=0,
            highlightthickness=0,
            width=25,
            pady=7
        )

        self.to_menu.pack()

        # ==========================================
        # INPUT
        # ==========================================

        input_label = tk.Label(
            self,
            text="Enter Value",
            font=("Segoe UI", 12, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        input_label.pack(pady=(15, 7))

        self.value_entry = tk.Entry(
            self,
            font=("Segoe UI", 18),
            bg="white",
            fg="#111111",
            bd=0,
            justify="center"
        )

        self.value_entry.pack(
            padx=45,
            fill="x",
            ipady=8
        )

        # ==========================================
        # BUTTONS
        # ==========================================

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )

        button_frame.pack(
            pady=20
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
            command=self.convert
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

        result_title = tk.Label(
            self,
            text="RESULT",
            font=("Segoe UI", 10, "bold"),
            bg="#f3f3f3",
            fg="#777777"
        )

        result_title.pack(
            pady=(0, 3)
        )

        self.result_label = tk.Label(
            self,
            text="--",
            font=("Segoe UI", 22, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )

        self.result_label.pack()

        # Set initial units
        self.update_units("Length")

    # ==========================================
    # UPDATE UNIT DROPDOWNS
    # ==========================================

    def update_units(self, category):

        unit_list = list(
            self.units[category].keys()
        )

        # Set default FROM unit
        self.from_var.set(
            unit_list[0]
        )

        # Set default TO unit
        if len(unit_list) > 1:
            self.to_var.set(
                unit_list[1]
            )
        else:
            self.to_var.set(
                unit_list[0]
            )

        # ==========================================
        # UPDATE FROM MENU
        # ==========================================

        from_menu = self.from_menu["menu"]

        from_menu.delete(
            0,
            "end"
        )

        for unit in unit_list:

            from_menu.add_command(
                label=unit,
                command=lambda value=unit:
                self.from_var.set(value)
            )

        # ==========================================
        # UPDATE TO MENU
        # ==========================================

        to_menu = self.to_menu["menu"]

        to_menu.delete(
            0,
            "end"
        )

        for unit in unit_list:

            to_menu.add_command(
                label=unit,
                command=lambda value=unit:
                self.to_var.set(value)
            )

    # ==========================================
    # TEMPERATURE CONVERSION
    # ==========================================

    def convert_temperature(
        self,
        value,
        from_unit,
        to_unit
    ):

        # First convert the temperature
        # into Celsius.

        if from_unit == "Celsius":

            celsius = value

        elif from_unit == "Fahrenheit":

            celsius = (
                value - 32
            ) * 5 / 9

        elif from_unit == "Kelvin":

            if value < 0:
                raise ValueError(
                    "Kelvin cannot be less than 0."
                )

            celsius = value - 273.15

        # Convert Celsius into target unit.

        if to_unit == "Celsius":

            return celsius

        elif to_unit == "Fahrenheit":

            return (
                celsius * 9 / 5
            ) + 32

        elif to_unit == "Kelvin":

            kelvin = celsius + 273.15

            if kelvin < 0:
                raise ValueError(
                    "Temperature cannot be below absolute zero."
                )

            return kelvin

    # ==========================================
    # MAIN CONVERSION FUNCTION
    # ==========================================

    def convert(self):

        # Get input
        value_text = (
            self.value_entry.get().strip()
        )

        # Check empty input
        if value_text == "":

            messagebox.showerror(
                "Missing Input",
                "Please enter a value."
            )

            return

        # Convert input to number
        try:

            value = float(value_text)

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid number."
            )

            return

        category = self.category_var.get()

        from_unit = self.from_var.get()

        to_unit = self.to_var.get()

        # ==========================================
        # TEMPERATURE
        # ==========================================

        if category == "Temperature":

            try:

                result = self.convert_temperature(
                    value,
                    from_unit,
                    to_unit
                )

            except ValueError as error:

                messagebox.showerror(
                    "Invalid Temperature",
                    str(error)
                )

                return

        # ==========================================
        # ALL OTHER CATEGORIES
        # ==========================================

        else:

            # Get conversion factors
            conversion_data = self.units[category]

            # Convert source value to base unit
            base_value = (
                value *
                conversion_data[from_unit]
            )

            # Convert base unit to target unit
            result = (
                base_value /
                conversion_data[to_unit]
            )

        # ==========================================
        # DISPLAY RESULT
        # ==========================================

        self.result_label.config(
            text=f"{result:.6g} {to_unit}"
        )

    # ==========================================
    # CLEAR
    # ==========================================

    def clear(self):

        self.value_entry.delete(
            0,
            tk.END
        )

        self.category_var.set(
            "Length"
        )

        self.update_units(
            "Length"
        )

        self.result_label.config(
            text="--"
        )


# ==============================================
# START APPLICATION
# ==============================================

if __name__ == "__main__":

    app = UnitConverter()

    app.mainloop()
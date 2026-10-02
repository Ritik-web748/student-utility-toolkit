import tkinter as tk
from tkinter import messagebox, filedialog

import qrcode
from PIL import ImageTk


class QRCodeGenerator(tk.Tk):

    def __init__(self):
        super().__init__()

        # Window settings
        self.title("QR Code Generator")
        self.geometry("500x680")
        self.minsize(500, 680)
        self.configure(bg="#f3f3f3")

        # Store the generated QR image
        self.qr_image = None

        # Store the Tkinter-compatible image
        self.tk_qr_image = None

        # Create the GUI
        self._build_ui()


    def _build_ui(self):

        # -------------------------
        # Title
        # -------------------------

        title = tk.Label(
            self,
            text="QR Code Generator",
            font=("Segoe UI", 24, "bold"),
            bg="#f3f3f3",
            fg="#111111"
        )
        title.pack(pady=(25, 10))


        # -------------------------
        # Instruction
        # -------------------------

        instruction = tk.Label(
            self,
            text="Enter text or a URL to generate a QR code",
            font=("Segoe UI", 12),
            bg="#f3f3f3",
            fg="#555555"
        )
        instruction.pack(pady=(0, 15))


        # -------------------------
        # Input Field
        # -------------------------

        self.input_entry = tk.Entry(
            self,
            font=("Segoe UI", 14),
            justify="center",
            bd=1
        )
        self.input_entry.pack(
            padx=40,
            fill="x",
            ipady=10
        )


        # -------------------------
        # Buttons
        # -------------------------

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        button_frame.pack(pady=20)


        generate_button = tk.Button(
            button_frame,
            text="Generate",
            font=("Segoe UI", 13, "bold"),
            bg="#ff9f0a",
            fg="#ffffff",
            bd=0,
            padx=25,
            pady=10,
            command=self.generate_qr
        )
        generate_button.grid(
            row=0,
            column=0,
            padx=6
        )


        save_button = tk.Button(
            button_frame,
            text="Save QR",
            font=("Segoe UI", 13, "bold"),
            bg="#d9d9d9",
            fg="#111111",
            bd=0,
            padx=25,
            pady=10,
            command=self.save_qr
        )
        save_button.grid(
            row=0,
            column=1,
            padx=6
        )


        clear_button = tk.Button(
            button_frame,
            text="Clear",
            font=("Segoe UI", 13, "bold"),
            bg="#d9d9d9",
            fg="#111111",
            bd=0,
            padx=25,
            pady=10,
            command=self.clear
        )
        clear_button.grid(
            row=0,
            column=2,
            padx=6
        )


        # -------------------------
        # QR Code Display Area
        # -------------------------

        self.qr_frame = tk.Frame(
            self,
            bg="#ffffff",
            bd=1,
            relief="solid",
            width=360,
            height=360
        )

        self.qr_frame.pack(
            padx=40,
            pady=10
        )

        # Prevent the frame from changing size
        # according to its contents.
        self.qr_frame.pack_propagate(False)


        self.qr_label = tk.Label(
            self.qr_frame,
            text="Your QR code will appear here",
            font=("Segoe UI", 12),
            bg="#ffffff",
            fg="#555555"
        )

        self.qr_label.pack(
            expand=True
        )


    # -------------------------
    # Generate QR Code
    # -------------------------

    def generate_qr(self):

        # Get the text or URL entered by the user
        data = self.input_entry.get().strip()


        # Check whether the input is empty
        if not data:
            messagebox.showerror(
                "Invalid Input",
                "Please enter some text or a URL."
            )
            return


        # Create the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4
        )


        # Add the user's data
        qr.add_data(data)

        # Automatically choose the QR code size
        qr.make(fit=True)


        # Create the QR image
        self.qr_image = qr.make_image(
            fill_color="black",
            back_color="white"
        ).convert("RGB")


        # Resize the image so it fits nicely
        # inside the GUI.
        display_image = self.qr_image.resize(
            (300, 300)
        )


        # Convert the PIL image into a format
        # that Tkinter can display.
        self.tk_qr_image = ImageTk.PhotoImage(
            display_image
        )


        # Display the QR code
        self.qr_label.config(
            image=self.tk_qr_image,
            text=""
        )


    # -------------------------
    # Save QR Code
    # -------------------------

    def save_qr(self):

        # Check whether a QR code exists
        if self.qr_image is None:
            messagebox.showerror(
                "No QR Code",
                "Please generate a QR code first."
            )
            return


        # Ask the user where to save the QR code
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[
                ("PNG Image", "*.png")
            ],
            title="Save QR Code"
        )


        # Save the original high-quality QR code
        if file_path:

            self.qr_image.save(file_path)

            messagebox.showinfo(
                "Saved",
                "QR code saved successfully."
            )


    # -------------------------
    # Clear Everything
    # -------------------------

    def clear(self):

        # Clear the input box
        self.input_entry.delete(
            0,
            tk.END
        )


        # Remove the stored QR image
        self.qr_image = None
        self.tk_qr_image = None


        # Reset the display area
        self.qr_label.config(
            image="",
            text="Your QR code will appear here"
        )


# -------------------------
# Start the application
# -------------------------

if __name__ == "__main__":

    app = QRCodeGenerator()

    app.mainloop()
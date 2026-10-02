import tkinter as tk
from tkinter import ttk, messagebox


class ExpenseTracker(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Expense Tracker")
        self.geometry("700x650")
        self.configure(bg="#f3f3f3")

        self.total_expense = 0

        self._build_ui()

    def _build_ui(self):

        tk.Label(
            self,
            text="Expense Tracker",
            font=("Segoe UI", 25, "bold"),
            bg="#f3f3f3"
        ).pack(pady=(25, 5))

        tk.Label(
            self,
            text="Track your expenses",
            font=("Segoe UI", 11),
            bg="#f3f3f3",
            fg="#555555"
        ).pack(pady=(0, 20))

        input_frame = tk.Frame(
            self,
            bg="#ffffff",
            bd=1,
            relief="solid"
        )
        input_frame.pack(
            padx=30,
            fill="x"
        )

        tk.Label(
            input_frame,
            text="Description",
            font=("Segoe UI", 11, "bold"),
            bg="#ffffff"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=(15, 5)
        )

        tk.Label(
            input_frame,
            text="Amount",
            font=("Segoe UI", 11, "bold"),
            bg="#ffffff"
        ).grid(
            row=0,
            column=1,
            padx=10,
            pady=(15, 5)
        )

        tk.Label(
            input_frame,
            text="Category",
            font=("Segoe UI", 11, "bold"),
            bg="#ffffff"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=(15, 5)
        )

        self.description_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11)
        )
        self.description_entry.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 15),
            ipady=6
        )

        self.amount_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11)
        )
        self.amount_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0, 15),
            ipady=6
        )

        self.category_var = tk.StringVar(
            value="Food"
        )

        category_menu = tk.OptionMenu(
            input_frame,
            self.category_var,
            "Food",
            "Travel",
            "Education",
            "Entertainment",
            "Shopping",
            "Bills",
            "Other"
        )

        category_menu.config(
            font=("Segoe UI", 10),
            bg="#f3f3f3"
        )

        category_menu.grid(
            row=1,
            column=2,
            padx=10,
            pady=(0, 15)
        )

        tk.Button(
            input_frame,
            text="Add Expense",
            font=("Segoe UI", 11, "bold"),
            bg="#ff9f0a",
            fg="white",
            bd=0,
            padx=15,
            pady=8,
            command=self.add_expense
        ).grid(
            row=1,
            column=3,
            padx=10,
            pady=(0, 15)
        )

        # Expense table

        table_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        table_frame.pack(
            padx=30,
            pady=25,
            fill="both",
            expand=True
        )

        columns = (
            "description",
            "amount",
            "category"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.tree.heading(
            "description",
            text="Description"
        )

        self.tree.heading(
            "amount",
            text="Amount"
        )

        self.tree.heading(
            "category",
            text="Category"
        )

        self.tree.column(
            "description",
            width=250
        )

        self.tree.column(
            "amount",
            width=120
        )

        self.tree.column(
            "category",
            width=150
        )

        self.tree.pack(
            fill="both",
            expand=True
        )

        # Buttons

        button_frame = tk.Frame(
            self,
            bg="#f3f3f3"
        )
        button_frame.pack(
            pady=10
        )

        tk.Button(
            button_frame,
            text="Delete Selected",
            font=("Segoe UI", 11, "bold"),
            bg="#555555",
            fg="white",
            bd=0,
            padx=15,
            pady=8,
            command=self.delete_selected
        ).grid(
            row=0,
            column=0,
            padx=5
        )

        tk.Button(
            button_frame,
            text="Clear All",
            font=("Segoe UI", 11, "bold"),
            bg="#d9d9d9",
            fg="#111111",
            bd=0,
            padx=25,
            pady=8,
            command=self.clear_all
        ).grid(
            row=0,
            column=1,
            padx=5
        )

        self.total_label = tk.Label(
            self,
            text="Total Expenses: ₹0.00",
            font=("Segoe UI", 18, "bold"),
            bg="#ffffff",
            bd=1,
            relief="solid",
            padx=20,
            pady=15
        )

        self.total_label.pack(
            padx=30,
            fill="x",
            pady=(5, 20)
        )

    def add_expense(self):

        description = (
            self.description_entry
            .get()
            .strip()
        )

        amount_text = (
            self.amount_entry
            .get()
            .strip()
        )

        category = self.category_var.get()

        if not description:

            messagebox.showerror(
                "Invalid Input",
                "Please enter an expense description."
            )

            return

        try:

            amount = float(
                amount_text
            )

            if amount <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Please enter a valid positive amount."
            )

            return

        self.tree.insert(
            "",
            tk.END,
            values=(
                description,
                f"₹{amount:.2f}",
                category
            )
        )

        self.total_expense += amount

        self.update_total()

        self.description_entry.delete(
            0,
            tk.END
        )

        self.amount_entry.delete(
            0,
            tk.END
        )

    def delete_selected(self):

        selected_items = self.tree.selection()

        if not selected_items:

            messagebox.showwarning(
                "No Selection",
                "Please select an expense to delete."
            )

            return

        for item in selected_items:

            values = self.tree.item(
                item,
                "values"
            )

            amount_text = values[1]

            amount = float(
                amount_text.replace(
                    "₹",
                    ""
                )
            )

            self.total_expense -= amount

            self.tree.delete(item)

        self.update_total()

    def clear_all(self):

        for item in self.tree.get_children():

            self.tree.delete(item)

        self.total_expense = 0

        self.update_total()

    def update_total(self):

        self.total_label.config(
            text=f"Total Expenses: ₹{self.total_expense:.2f}"
        )


if __name__ == "__main__":

    app = ExpenseTracker()
    app.mainloop()
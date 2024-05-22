import mysql.connector
import tkinter as tk
from tkinter import messagebox

class NovaStock:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

        # Initialize GUI with maroon and orange theme
        self.root = tk.Tk()
        self.root.title("NovaStock Inventory Management")
        self.root.geometry("400x400")
        self.root.configure(bg="maroon")

        # Create main frame
        self.main_frame = tk.Frame(self.root, bg="maroon")
        self.main_frame.pack(pady=10)

        # Welcome label
        self.label = tk.Label(self.main_frame, text="Welcome to NovaStock", font=("Helvetica", 16), bg="maroon", fg="orange")
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        # Add Item button
        self.add_button = tk.Button(self.main_frame, text="Add Item", command=self.add_item, width=15, bg="orange", fg="maroon")
        self.add_button.grid(row=1, column=0, padx=5, pady=5)

        # View Items button
        self.view_button = tk.Button(self.main_frame, text="View Items", command=self.view_items, width=15, bg="orange", fg="maroon")
        self.view_button.grid(row=1, column=1, padx=5, pady=5)

        # Reset button
        self.reset_button = tk.Button(self.main_frame, text="Reset All", command=self.reset_items, width=15, bg="orange", fg="maroon")
        self.reset_button.grid(row=1, column=2, padx=5, pady=5)

        self.root.mainloop()

    def add_item(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Add Item")
        self.add_window.configure(bg="maroon")

        self.name_label = tk.Label(self.add_window, text="Name:", bg="maroon", fg="orange")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.add_window)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.quantity_label = tk.Label(self.add_window, text="Quantity:", bg="maroon", fg="orange")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(self.add_window)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=5)

        self.price_label = tk.Label(self.add_window, text="Price:", bg="maroon", fg="orange")
        self.price_label.grid(row=2, column=0, padx=10, pady=5)
        self.price_entry = tk.Entry(self.add_window)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_submit_button = tk.Button(self.add_window, text="Add", command=self.add_item_to_database, bg="orange", fg="maroon")
        self.add_submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_item_to_database(self):
        name = self.name_entry.get()
        quantity = int(self.quantity_entry.get())
        price = float(self.price_entry.get())

        sql = "INSERT INTO items (name, quantity, price) VALUES (%s, %s, %s)"
        val = (name, quantity, price)
        self.cursor.execute(sql, val)
        self.conn.commit()
        messagebox.showinfo("Success", "Item added successfully!")
        self.add_window.destroy()

    def view_items(self):
        self.view_window = tk.Toplevel(self.root)
        self.view_window.title("View Items")
        self.view_window.configure(bg="maroon")

        self.cursor.execute("SELECT * FROM items")
        result = self.cursor.fetchall()

        total_items = sum(row[2] for row in result)  # Calculate total number of items in stock

        tk.Label(self.view_window, text=f"Total items in stock: {total_items}", bg="maroon", fg="orange").grid(row=0, column=0, columnspan=5, pady=5)

        # Display headers
        headers = ["ID", "Name", "Quantity", "Price", ""]
        for col_index, header in enumerate(headers):
            tk.Label(self.view_window, text=header, font=("Helvetica", 10, "bold"), bg="maroon", fg="orange").grid(row=1, column=col_index, padx=5, pady=3)

        # Display item details
        for row_index, row in enumerate(result, start=2):
            for col_index, value in enumerate(row):
                tk.Label(self.view_window, text=value, bg="maroon", fg="orange").grid(row=row_index, column=col_index, padx=5, pady=3)
            delete_button = tk.Button(self.view_window, text="Delete", command=lambda r=row[0]: self.delete_item(r), bg="orange", fg="maroon")
            delete_button.grid(row=row_index, column=4, padx=5, pady=3)

    def delete_item(self, item_id):
        if messagebox.askyesno("Confirmation", "Are you sure you want to delete this item?"):
            sql = "DELETE FROM items WHERE id = %s"
            self.cursor.execute(sql, (item_id,))
            self.conn.commit()
            messagebox.showinfo("Success", "Item deleted successfully!")
            self.view_window.destroy()
            self.view_items()

    def reset_items(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to reset all items? This action cannot be undone."):
            sql = "DELETE FROM items"
            self.cursor.execute(sql)
            self.conn.commit()
            messagebox.showinfo("Success", "All items have been reset!")
            self.view_window.destroy()
            self.view_items()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    # Replace the host, user, password, and database values below with your MySQL server details
    novastock = NovaStock(host="localhost", user="root", password="", database="inventory")

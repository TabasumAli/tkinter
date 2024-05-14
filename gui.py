# gui.py

import tkinter as tk
from tkinter import messagebox
from database import Database

class EmployeeGUI:
    def __init__(self, master):
        self.master = master
        self.db = Database()
        self.create_widgets()

    def create_widgets(self):
        self.employee_listbox = tk.Listbox(self.master)
        self.employee_listbox.pack()

        self.refresh_button = tk.Button(self.master, text="Refresh", command=self.refresh_employee_list)
        self.refresh_button.pack()

        self.add_button = tk.Button(self.master, text="Add Employee", command=self.add_employee)
        self.add_button.pack()

        self.update_button = tk.Button(self.master, text="Update Employee", command=self.update_employee)
        self.update_button.pack()

        self.delete_button = tk.Button(self.master, text="Delete Employee", command=self.delete_employee)
        self.delete_button.pack()

        self.refresh_employee_list()

    def refresh_employee_list(self):
        self.employee_listbox.delete(0, tk.END)
        employees = self.db.get_employees()
        for employee in employees:
            self.employee_listbox.insert(tk.END, f"{employee[0]}: {employee[1]} - {employee[2]} - {employee[3]}")

    def add_employee(self):
        # Implement functionality to add a new employee
        pass

    def update_employee(self):
        # Implement functionality to update an employee
        pass

    def delete_employee(self):
        # Implement functionality to delete an employee
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeGUI(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
from backend import StaffDB

class StaffManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Staff Information Management System")

        self.staff_db = StaffDB()


        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Qualifications:").grid(row=2, column=0, padx=5, pady=5)
        self.qualifications_entry = tk.Entry(self.root)
        self.qualifications_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Role:").grid(row=3, column=0, padx=5, pady=5)
        self.role_entry = tk.Entry(self.root)
        self.role_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Contact Number:").grid(row=4, column=0, padx=5, pady=5)
        self.contact_entry = tk.Entry(self.root)
        self.contact_entry.grid(row=4, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.root, text="Add Staff", command=self.add_staff)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.tree = ttk.Treeview(self.root, columns=('ID', 'Name', 'Age', 'Qualifications', 'Role', 'Contact Number'))
        self.tree.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='Name')
        self.tree.heading('#2', text='Age')
        self.tree.heading('#3', text='Qualifications')
        self.tree.heading('#4', text='Role')
        self.tree.heading('#5', text='Contact Number')

        self.update_treeview()

        self.edit_button = tk.Button(self.root, text="Edit Staff", command=self.edit_staff)
        self.edit_button.grid(row=7, column=0, pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Staff", command=self.delete_staff)
        self.delete_button.grid(row=7, column=1, pady=5)

    def add_staff(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        qualifications = self.qualifications_entry.get()
        role = self.role_entry.get()
        contact_number = self.contact_entry.get()

        if name and age and qualifications and role and contact_number:
            self.staff_db.add_staff(name, age, qualifications, role, contact_number)
            self.update_treeview()


            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.qualifications_entry.delete(0, tk.END)
            self.role_entry.delete(0, tk.END)
            self.contact_entry.delete(0, tk.END)

    def update_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        staff_data = self.staff_db.get_all_staff()

        for row in staff_data:
            self.tree.insert('', 'end', values=row)

    def edit_staff(self):
        selected_item = self.tree.selection()
        if selected_item:
            staff_data = self.tree.item(selected_item, 'values')
            staff_id, name, age, qualifications, role, contact_number = staff_data


            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, name)

            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, age)

            self.qualifications_entry.delete(0, tk.END)
            self.qualifications_entry.insert(0, qualifications)

            self.role_entry.delete(0, tk.END)
            self.role_entry.insert(0, role)

            self.contact_entry.delete(0, tk.END)
            self.contact_entry.insert(0, contact_number)


            self.add_button.configure(text="Save Changes", command=lambda: self.save_changes(staff_id))

    def save_changes(self, staff_id):
        name = self.name_entry.get()
        age = self.age_entry.get()
        qualifications = self.qualifications_entry.get()
        role = self.role_entry.get()
        contact_number = self.contact_entry.get()

        if name and age and qualifications and role and contact_number:
            self.staff_db.update_staff(staff_id, name, age, qualifications, role, contact_number)
            self.update_treeview()


            self.name_entry.delete(0, tk.END)
            self.age_entry.delete(0, tk.END)
            self.qualifications_entry.delete(0, tk.END)
            self.role_entry.delete(0, tk.END)
            self.contact_entry.delete(0, tk.END)

            self.add_button.configure(text="Add Staff", command=self.add_staff)

    def delete_staff(self):
        selected_item = self.tree.selection()
        if selected_item:
            staff_id = self.tree.item(selected_item, 'values')[0]
            self.staff_db.delete_staff(staff_id)
            self.update_treeview()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = StaffManagementApp(root)
    app.run()
    app.staff_db.close_connection()

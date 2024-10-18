# Contact Book
import tkinter as tk
from tkinter import messagebox, simpledialog

# In-memory contact list (acting as a simple database)
contacts = {}

# Function to add a new contact
def add_contact():
    store_name = entry_store_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if store_name and phone:
        contacts[store_name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Success", f"Contact {store_name} added!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showerror("Error", "Store name and phone number are required.")

# Function to display all contacts
def display_contacts():
    listbox_contacts.delete(0, tk.END)
    for store_name, details in contacts.items():
        listbox_contacts.insert(tk.END, f"{store_name} - {details['phone']}")

# Function to search for a contact by store name or phone number
def search_contact():
    search_term = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)

    for store_name, details in contacts.items():
        if search_term in store_name.lower() or search_term in details['phone']:
            listbox_contacts.insert(tk.END, f"{store_name} - {details['phone']}")

    if listbox_contacts.size() == 0:
        messagebox.showinfo("No Results", "No contacts found.")

# Function to update a selected contact
def update_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE).split(' - ')[0]
    if selected_contact in contacts:
        new_phone = simpledialog.askstring("Input", f"Update phone for {selected_contact}:", initialvalue=contacts[selected_contact]['phone'])
        new_email = simpledialog.askstring("Input", f"Update email for {selected_contact}:", initialvalue=contacts[selected_contact]['email'])
        new_address = simpledialog.askstring("Input", f"Update address for {selected_contact}:", initialvalue=contacts[selected_contact]['address'])
        
        contacts[selected_contact] = {'phone': new_phone, 'email': new_email, 'address': new_address}
        messagebox.showinfo("Success", f"Contact {selected_contact} updated!")
        display_contacts()

# Function to delete a selected contact
def delete_contact():
    selected_contact = listbox_contacts.get(tk.ACTIVE).split(' - ')[0]
    if selected_contact in contacts:
        del contacts[selected_contact]
        messagebox.showinfo("Success", f"Contact {selected_contact} deleted!")
        display_contacts()

# Function to clear entry fields after adding a contact
def clear_entries():
    entry_store_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Contact Book")

# Labels and entry fields for contact details
label_store_name = tk.Label(window, text="Store Name:", font=('Arial', 12))
label_store_name.grid(row=0, column=0, padx=10, pady=10)
entry_store_name = tk.Entry(window)
entry_store_name.grid(row=0, column=1, padx=10, pady=10)

label_phone = tk.Label(window, text="Phone Number:", font=('Arial', 12))
label_phone.grid(row=1, column=0, padx=10, pady=10)
entry_phone = tk.Entry(window)
entry_phone.grid(row=1, column=1, padx=10, pady=10)

label_email = tk.Label(window, text="Email:", font=('Arial', 12))
label_email.grid(row=2, column=0, padx=10, pady=10)
entry_email = tk.Entry(window)
entry_email.grid(row=2, column=1, padx=10, pady=10)

label_address = tk.Label(window, text="Address:", font=('Arial', 12))
label_address.grid(row=3, column=0, padx=10, pady=10)
entry_address = tk.Entry(window)
entry_address.grid(row=3, column=1, padx=10, pady=10)

# Buttons to add, update, and delete contacts
button_add = tk.Button(window, text="Add Contact", command=add_contact, bg="#4CAF50", fg="white", font=('Arial', 12))
button_add.grid(row=4, column=0, columnspan=2, pady=10)

button_update = tk.Button(window, text="Update Contact", command=update_contact, bg="#2196F3", fg="white", font=('Arial', 12))
button_update.grid(row=5, column=0, columnspan=2, pady=10)

button_delete = tk.Button(window, text="Delete Contact", command=delete_contact, bg="#f44336", fg="white", font=('Arial', 12))
button_delete.grid(row=6, column=0, columnspan=2, pady=10)

# Listbox to display contacts
listbox_contacts = tk.Listbox(window, width=50, height=10)
listbox_contacts.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Search field and button
entry_search = tk.Entry(window)
entry_search.grid(row=8, column=0, padx=10, pady=10)

button_search = tk.Button(window, text="Search Contact", command=search_contact, bg="#FF9800", fg="white", font=('Arial', 12))
button_search.grid(row=8, column=1, padx=10, pady=10)

# Initialize the contact list display
display_contacts()

# Start the GUI event loop
window.mainloop()

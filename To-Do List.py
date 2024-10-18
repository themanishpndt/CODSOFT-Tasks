# To-Do List
import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "✔" if self.completed else "✘"
        return f"{self.description} (Due: {self.due_date}) [{status}]"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.configure(bg='#e3f2fd')  # Light blue background
        self.tasks = self.load_tasks()

        # Frame for 3D effect
        self.frame = tk.Frame(root, bg='#bbdefb', bd=5, relief=tk.RIDGE)
        self.frame.pack(pady=20, padx=20)

        # 3D-style Listbox for tasks
        self.task_listbox = tk.Listbox(self.frame, width=50, height=15, bg='#ffffff', fg='#333333',
                                       selectbackground='#64b5f6', font=("Arial", 12), bd=5, relief=tk.SUNKEN)
        self.task_listbox.pack(pady=10, padx=10)

        # Add Task button with 3D-like appearance
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, bg='#4caf50', fg='white', 
                                    font=("Arial", 12, 'bold'), bd=4, relief=tk.RAISED)
        self.add_button.pack(pady=5)

        # Update Task button
        self.update_button = tk.Button(root, text="Update Task", command=self.update_task, bg='#2196f3', fg='white', 
                                       font=("Arial", 12, 'bold'), bd=4, relief=tk.RAISED)
        self.update_button.pack(pady=5)

        # Delete Task button
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, bg='#f44336', fg='white', 
                                       font=("Arial", 12, 'bold'), bd=4, relief=tk.RAISED)
        self.delete_button.pack(pady=5)

        self.load_tasks_to_listbox()

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks_data = json.load(file)
                return [Task(**data) for data in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)

    def load_tasks_to_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def add_task(self):
        description = simpledialog.askstring("Add Task", "Enter task description:")
        due_date = simpledialog.askstring("Add Task", "Enter due date (optional):")
        if description:
            task = Task(description, due_date)
            self.tasks.append(task)
            self.save_tasks()
            self.load_tasks_to_listbox()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            task = self.tasks[index]
            new_description = simpledialog.askstring("Update Task", "New description:", initialvalue=task.description)
            new_due_date = simpledialog.askstring("Update Task", "New due date (optional):", initialvalue=task.due_date)
            if new_description:
                task.description = new_description
                task.due_date = new_due_date
                self.save_tasks()
                self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Update Task", "Select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks.pop(index)
            self.save_tasks()
            self.load_tasks_to_listbox()
        else:
            messagebox.showwarning("Delete Task", "Select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        
        # Set the background color of the main window
        self.root.configure(bg="#f0f0f0")
        
        self.tasks = []
        
        # Create and place widgets
        self.frame = tk.Frame(root, bg="#ffffff", padx=10, pady=10)
        self.frame.pack(padx=10, pady=10)
        
        self.task_entry = tk.Entry(self.frame, width=40, bg="#e6e6e6", borderwidth=2)
        self.task_entry.grid(row=0, column=0, padx=5, pady=5)
        
        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.grid(row=0, column=1, padx=5, pady=5)
        
        self.edit_button = tk.Button(self.frame, text="Edit Task", command=self.edit_task, bg="#2196F3", fg="white")
        self.edit_button.grid(row=0, column=2, padx=5, pady=5)
        
        self.remove_button = tk.Button(self.frame, text="Remove Task", command=self.remove_task, bg="#f44336", fg="white")
        self.remove_button.grid(row=0, column=3, padx=5, pady=5)
        
        self.task_listbox = tk.Listbox(self.frame, width=60, height=15, selectmode=tk.SINGLE, bg="#ffffff", borderwidth=2)
        self.task_listbox.grid(row=1, column=0, columnspan=4, padx=5, pady=5)
        
        self.update_task_list()
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_entry.delete(0, tk.END)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")
    
    def edit_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            new_task = simpledialog.askstring("Edit Task", "Edit the selected task:", initialvalue=self.tasks[task_index])
            if new_task:
                self.tasks[task_index] = new_task
                self.update_task_list()
        else:
            messagebox.showwarning("Warning", "No task selected")
    
    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.tasks.pop(task_index)
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "No task selected")
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for idx, task in enumerate(self.tasks, 1):
            self.task_listbox.insert(tk.END, f"{idx}. {task}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

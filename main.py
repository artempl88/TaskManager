import tkinter as tk
from tkinter import ttk
import datetime

class TaskManagerApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Task Manager")
        self.geometry("400x400")
        self.resizable(False, False)
        
        self.tasks = []
        
        tk.Label(self, text="Add a task").grid(row=0, column=0, sticky="W", padx=10, pady=10)
        tk.Label(self, text="Task name").grid(row=1, column=0, sticky="W", padx=10)
        self.task_name = tk.Entry(self)
        self.task_name.grid(row=1, column=1, padx=10)
        tk.Label(self, text="Due date").grid(row=2, column=0, sticky="W", padx=10)
        self.due_date = tk.Entry(self)
        self.due_date.grid(row=2, column=1, padx=10)
        tk.Label(self, text="Priority").grid(row=3, column=0, sticky="W", padx=10)
        self.priority = tk.Entry(self)
        self.priority.grid(row=3, column=1, padx=10)
        self.add_button = tk.Button(self, text="Add", command=self.add_task)
        self.add_button.grid(row=4, column=1, padx=10, pady=10)
        
        self.tasks_tree = ttk.Treeview(self, columns=("due_date", "priority", "completion"))
        self.tasks_tree.heading("#0", text="Task name", anchor="w")
        self.tasks_tree.heading("due_date", text="Due date", anchor="w")
        self.tasks_tree.heading("priority", text="Priority", anchor="w")
        self.tasks_tree.heading("completion", text="Completion", anchor="w")
        self.tasks_tree.column("#0", width=200, minwidth=200, stretch=tk.NO)
        self.tasks_tree.column("due_date", width=100, minwidth=100, stretch=tk.NO)
        self.tasks_tree.column("priority", width=100, minwidth=100, stretch=tk.NO)
        self.tasks_tree.column("completion", width=100, minwidth=100, stretch=tk.NO)
        self.tasks_tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        self.sort_by = tk.StringVar(self)
        sort_options = ["Due date", "Priority", "Completion"]
        self.sort_by.set("Due date")
        sort_dropdown = tk.OptionMenu(root, sort_var, *sort_options)
        sort_dropdown.pack(pady=10)
        sort_button = tk.Button(root, text="Sort", command=sort_tasks)
        sort_button.pack()

        task_list = tk.Listbox(root)
        task_list.pack(pady=10, fill="both", expand=True)

        add_task_frame = tk.Frame(root)
        add_task_frame.pack(pady=10)

        task_entry = tk.Entry(add_task_frame)
        task_entry.pack(side="left", fill="x", expand=True)

        add_task_button = tk.Button(add_task_frame, text="Add Task", command=add_task)
        add_task_button.pack(side="right")

root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from my_canvas import my_canvas

import json


class menu(tk.Menu):
    def __init__(self, frame):
        super().__init__(frame)
        self.master_app = frame  # this is for calling function of its master (master_app)

        # Create file menu
        self.file_menu = tk.Menu(self)
        self.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="Import", command=self.import_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)

        # Create edit menu
        self.edit_menu = tk.Menu(self)
        self.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="size", command=self.size)
        self.edit_menu.add_command(label="color", command=self.color)

    def import_file(self):
        file_path = filedialog.askopenfile(
            title="Select File",
            initialdir="/",
            filetypes=(("JSON files", "*.json"),)
        )

        with open(file_path.name, 'r') as f:
            data = json.load(f)

        try:
            new_x = data["columns"]
            new_y = data["rows"]
            new_data = data["data"]
        except KeyError:
            messagebox.showwarning(title="Error",
                                   message=f"Unrecognized file\n{file_path.name}")
        else:
            self.master_app.canvas.destroy()
            self.master_app.canvas = my_canvas(self.master_app, new_x, new_y)
            self.master_app.data = new_data
            self.master_app.canvas.update()
            print(self.master_app)
        pass

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            title="Save file",
            initialdir="/",
            filetypes=(("JSON files", "*.json"),)
        )

        file_path += ".json"

        stored_data = {
            "rows": self.master_app.grid_y,
            "columns": self.master_app.grid_x,
            "data": self.master_app.data
        }
        with open(file_path, 'w') as f:
            json.dump(stored_data, f)

    def size(self):
        # Create a new window to display grid size information
        change_size_window = tk.Toplevel(self.master_app.master)
        change_size_window.title("change size")

        # create two entry to for rows and columns
        row_label = tk.Label(change_size_window, text="Rows:")
        row_label.grid(row=0, column=0)
        row_entry = tk.Entry(change_size_window, width=20, borderwidth=7)
        row_entry.grid(row=0, column=1, columnspan=1)

        columns_label = tk.Label(change_size_window, text="Columns:")
        columns_label.grid(row=1, column=0)
        columns_entry = tk.Entry(change_size_window, width=20, borderwidth=7)
        columns_entry.grid(row=1, column=1, columnspan=1)

        def size_command(command: int):
            nonlocal change_size_window
            if command == 1:
                try:
                    x = int(columns_entry.get())
                    y = int(row_entry.get())
                    if x <= 0 or y <= 0:
                        raise ValueError
                except ValueError:
                    error_label = tk.Label(change_size_window, text="Integer above 0 only")
                    error_label.grid(row=2, column=0)
                else:
                    self.master_app.grid_x = x
                    self.master_app.grid_y = y

                    self.master_app.canvas.destroy()
                    self.master_app.canvas = my_canvas(self.master_app, x, y)

                    change_size_window.destroy()
            else:
                change_size_window.destroy()

        # Create a button to close the window
        button1 = tk.Button(change_size_window, text="Cancel", command=lambda: size_command(0))
        button2 = tk.Button(change_size_window, text="Save", command=lambda: size_command(1))
        button1.grid(row=3, column=0)
        button2.grid(row=3, column=1)

    def color(self):
        # TO DO: implement redo functionality
        pass

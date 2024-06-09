import tkinter as tk
from my_canvas import my_canvas


class menu(tk.Menu):
    def __init__(self, frame):
        super().__init__(frame)
        self.frame = frame  # this is for calling function of its master (frame)

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
        # TO DO: implement import file functionality
        self.frame.canvas.destroy()
        pass

    def save_file(self):
        # TO DO: implement save file functionality
        pass

    def size(self):
        # Create a new window to display grid size information
        undo_window = tk.Toplevel(self.frame.master)
        undo_window.title("change size")

        # create two entry to for rows and columns
        row_label = tk.Label(undo_window, text="Rows:")
        row_label.grid(row=0, column=0)
        row_entry = tk.Entry(undo_window, width=20, borderwidth=7)
        row_entry.grid(row=0, column=1, columnspan=1)

        columns_label = tk.Label(undo_window, text="Columns:")
        columns_label.grid(row=1, column=0)
        columns_entry = tk.Entry(undo_window, width=20, borderwidth=7)
        columns_entry.grid(row=1, column=1, columnspan=1)

        def size_command(command: int):
            nonlocal undo_window
            if command == 1:
                try:
                    x = int(columns_entry.get())
                    y = int(row_entry.get())
                    if x <= 0 or y <= 0:
                        raise ValueError
                except ValueError:
                    error_label = tk.Label(undo_window, text="Integer above 0 only")
                    error_label.grid(row=2, column=0)
                else:
                    self.frame.grid_x = x
                    self.frame.grid_y = y

                    self.frame.canvas.destroy()
                    self.frame.canvas = my_canvas(self.frame, x, y)

                    undo_window.destroy()
            else:
                undo_window.destroy()

        # Create a button to close the window
        button1 = tk.Button(undo_window, text="Cancel", command=lambda: size_command(0))
        button2 = tk.Button(undo_window, text="Save", command=lambda: size_command(1))
        button1.grid(row=3, column=0)
        button2.grid(row=3, column=1)

    def color(self):
        # TO DO: implement redo functionality
        pass

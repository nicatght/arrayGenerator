import tkinter as tk
from my_canvas import my_canvas
from menuFunction import menu


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        # Create menu
        self.menu = menu(self)
        self.master.config(menu=self.menu)

        # initialized value (can be change later on)
        self.grid_x = 48
        self.grid_y = 26
        self.grid_pad = 20

        self.canvas = my_canvas(self, self.grid_x, self.grid_y)

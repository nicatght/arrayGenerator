import tkinter as tk


class my_canvas(tk.Canvas):
    def __init__(self, master, x, y, **kwargs):
        # reconstruct root size
        size = str(x * 20) + "x" + str(y * 20)
        master.master.geometry(size)
        master.data = [0] * (x * y)
        super().__init__(master,
                         width=x * 20,
                         height=y * 20,
                         bg="white",
                         **kwargs)

        self.master = master  # master is app
        self.master.grid_x = x
        self.master.grid_y = y

        self.generate_grid(x, y, 20)

        # Bind click and hold events to canvas
        self.bind("<Button-1>", lambda event: self.change_color(event, 0))
        self.bind("<B1-Motion>", lambda event: self.change_color(event, 0))

        self.bind("<Button-3>", lambda event: self.change_color(event, 1))
        self.bind("<B3-Motion>", lambda event: self.change_color(event, 1))

        self.pack(padx=0, pady=0)

    def update(self) -> None:
        """
        This function force update the canvas according to app's data
        :return: None
        """
        local_data = self.master.data
        print(local_data)
        for y in range(self.master.grid_y):
            for x in range(self.master.grid_x):
                if local_data[self.master.grid_x * y + x] == 1:
                    color = "blue"
                else:
                    color = "white"
                self.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill=color)

    def generate_grid(self, x, y, pad):
        for i in range(0, x * pad, pad):
            self.create_line(i, 0, i, y * pad, fill="black")
        for i in range(0, y * pad, pad):
            self.create_line(0, i, x * pad, i, fill="black")

    def change_color(self, event, input: int):
        x, y = event.x, event.y
        x //= 20
        y //= 20
        if x >= self.master.grid_x or y >= self.master.grid_y:
            return

        array_location = x * self.master.grid_y + y

        if input == 0:
            color = "blue"
            self.master.data[array_location] = 1
        else:
            color = "white"
            self.master.data[array_location] = 0

        self.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill=color)

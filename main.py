import tkinter as tk
from app import App


def main():
    root = tk.Tk()
    root.geometry("960x520")
    app = App(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
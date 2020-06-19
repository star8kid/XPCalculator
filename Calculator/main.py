from tkinter import *
from tkinter import ttk


class StartApp():
    def __init__(self):
        self.root = Tk()

        self.menu_window = ttk.Frame(self.root, padding = "10 10 10 10")

        self.menuButton1 = ttk.Button(self.menu_window)
        self.menuButton1.grid( row = 1 ,column = 1)

        self.menu_window.pack()




if __name__ == "__main__":
    app = StartApp()
    app.root.title("XPCalculator")
    app.root.mainloop()

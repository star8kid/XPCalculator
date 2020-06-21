from tkinter import *
from tkinter import ttk
from tkinter import font
import time


class StartApp():
    def __init__(self):

        # 1. All the window and button definitions
        self.root = Tk()



        
        self.menu_window = ttk.Frame(self.root, padding = "100 10 100 10")
        self.title_font = font.Font( family = "System", size = 18 , weight = "bold")
        self.title_label = ttk.Label(self.menu_window, text = "XP Calculator", font = self.title_font, padding = "5 20 5 50")
        self.title_label.grid(row = 0 , column = 1)

        self.padVerticalValue = 3
        self.menuButton1 = ttk.Button(self.menu_window)
        self.menuButton1.grid( row = 1 , column = 1 , pady = self.padVerticalValue)
        self.menuButton2 = ttk.Button(self.menu_window)
        self.menuButton2.grid( row = 2 , column = 1 , pady = self.padVerticalValue)
        self.menuButton3 = ttk.Button(self.menu_window)
        self.menuButton3.grid( row = 3 , column = 1 , pady = self.padVerticalValue)
        self.menuQuit = ttk.Button(self.menu_window)
        self.menuQuit.grid( row = 4, column = 1 , pady = self.padVerticalValue)


        self.from_zero_window = Toplevel()
        self.from_zero_window.title("Calculate From Level Zero")
        




        # 2. The button configurations

        self.menuButton1.config( text = "Calculate From Level Zero", command = lambda : self.openCalcZero())

        self.quitStyle = ttk.Style()
        self.quitStyle.configure("Quit.TButton", foreground = "dark red")
        self.menuQuit.config( text = "Quit" , style = "Quit.TButton" , command = lambda : self.root.quit())

        self.from_zero_window.withdraw()

        self.menu_window.pack()
    # 3. The method configurations

    def openCalcZero(self):
        self.from_zero_window.deiconify()
        self.from_zero_window.mainloop()






if __name__ == "__main__":
    app = StartApp()
    app.root.title("XPCalculator")
    print(font.families())
    app.root.mainloop()


    # print(font.families())  < - - Use this if you want to print the font familes th are stored on your computer
   
    
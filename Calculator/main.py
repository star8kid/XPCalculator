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


        




        # 2. The button configurations


        self.quitStyle = ttk.Style()
        self.quitStyle.configure("Quit.TButton", foreground = "dark red")
        self.menuQuit.config( text = "Quit" , style = "Quit.TButton" , command = lambda : self.root.quit())

     

        self.menu_window.pack()
    # 3. The method definitions/configurations

    def openFeatureWindow(self, window_referance):
        window_referance.deiconify()
        window_referance.mainloop()



class FromLevelZero():
    def __init__(self, feature_title):

        self.feature_title = feature_title
        self.root = Tk()
    
        self.title_frame = ttk.Frame(self.root, padding = "50 10 50 10")
        self.feature1_font = font.Font( family = "Times New Roman", size = 12 , weight = "bold")
        self.title_label = ttk.Label(self.title_frame, text = "From Level Zero", font = self.feature1_font, padding = "40 50 40 100")
        self.title_label.grid( row = 1 , column = 1)
        self.title_frame.pack()


        # For this feature of the program, the software will allow an input of
        # a single level integer and calculate the amount of experience required to reach that level from level 0
        self.feature_frame = ttk.Frame(self.root, padding = "10 10 10 10")
        self.feature_frame.pack()

        self.targetLevel = StringVar()
        self.totalNeededXPNum = StringVar()

        



        




if __name__ == "__main__":

    #App initialization
    app = StartApp()
    feature1 = FromLevelZero("Calculate From Level Zero")
    feature1.root.withdraw()

    #Window Configurations
    app.root.title("XPCalculator")
    feature1.root.title(feature1.feature_title)

    app.menuButton1.config( text = feature1.feature_title, command = lambda : app.openFeatureWindow(feature1.root) )



    #Start of the app
    app.root.mainloop()


    #print(font.families())  
    # ^^^^^^^ Use this if you want to print the font familes th are stored on your computer
   
    
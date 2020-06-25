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
    def openMenuWindow(self):
        self.root.deiconify()
        self.root.mainloop()



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

     
        self.inputLabel = ttk.Label(self.feature_frame, text = "Input the target level you're trying to reach: ")
        self.inputLabel.grid( row = 2 , column = 0)
        self.outputLabel = ttk.Label(self.feature_frame, text = "The amount of experience needed to reach that level is: ")
        self.outputLabel.grid( row = 3, column = 0)
        self.levelEntry = ttk.Entry(self.feature_frame, width = 15 , textvariable = self.targetLevel)
        self.levelEntry.grid( row = 2 , column = 1)
        self.neededExpLabel = ttk.Label(self.feature_frame, textvariable = self.totalNeededXPNum)
        self.neededExpLabel.grid( row = 3, column = 1)
        self.calcButton = ttk.Button(self.feature_frame, text = "Calculate!", command = self.lvlZeroSet)
        self.calcButton.grid( row = 4 , column = 1)
      



    #Figure out how to set the calculated number into the label!!!!!!!!!!!
    def lvlZeroSet(self):
        try: 
            print("This func has been called!!\n")
            self.totalNeededXPNum.set("I can display things!")
            #print("The total amount of exp you've entered is " + self.totalNeededXPNum.get() + "\n")
        except ValueError:
            print("Please input a valid value!!")
            pass

    def lvlZeroCalculate(self):
        try:
            target = float(self.levelEntry.get())
            neededExp = 0
            if(target >= 0 and target <= 16):
                neededExp = (target ** 2) + (target * 6)
                self.totalNeededXPNum.set(str(neededExp))
                print("The amount of exp needed is " + self.totalNeededXPNum.get() + "\n")
                return self.totalNeededXPNum
            elif(target >= 17 and target <= 31):
                neededExp = (((target ** 2) * 2.5) - (target * 40.5)) + 360
                self.totalNeededXPNum.set(str(neededExp))
                return self.totalNeededXPNum
            elif(target>= 32):
                neededExp = (((target ** 2) * 4.5) - (target * 162.5)) + 2220
                self.totalNeededXPNum.set(str(neededExp))
                return self.totalNeededXPNum
        except ValueError:
            print("Please input a correct value!")
            pass
       
    
# Figure out how to do the calculation function for this feature
        



        




if __name__ == "__main__":

    #App initialization
    app = StartApp()
    feature1 = FromLevelZero("Calculate From Level Zero")
    feature1.root.withdraw()

    #Window Configurations
    app.root.title("XPCalculator")
    feature1.root.title(feature1.feature_title)

    app.menuButton1.config( text = feature1.feature_title, command = lambda : app.openFeatureWindow(feature1.root) )


    feature1.root.bind('<Return>', feature1.lvlZeroSet)


    #Start of the app
    app.root.mainloop()


    #print(font.families())  
    # ^^^^^^^ Use this if you want to print the font familes th are stored on your computer
   
    
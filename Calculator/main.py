from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import math




class StartApp():
    def __init__(self):

        # 1. All the window and button definitions
        self.root = Tk()
        self.menu_window = ttk.Frame(self.root, padding = "100 10 100 10")
        self.title_font = font.Font( family = "System", size = 18 , weight = "bold")
        self.title_label = ttk.Label(self.menu_window, text = "XP Calculator", font = self.title_font, padding = "5 20 5 50")
        self.title_label.grid(row = 0 , column = 1)

        self.padVerticalValue = 3
        self.menuButtonWidth = 35
        self.menuButton1 = ttk.Button(self.menu_window, width = self.menuButtonWidth)
        self.menuButton1.grid( row = 1 , column = 1 , pady = self.padVerticalValue)
        self.menuButton2 = ttk.Button(self.menu_window, width = self.menuButtonWidth)
        self.menuButton2.grid( row = 2 , column = 1 , pady = self.padVerticalValue)
        self.menuButton3 = ttk.Button(self.menu_window, width = self.menuButtonWidth)
        self.menuButton3.grid( row = 3 , column = 1 , pady = self.padVerticalValue)
        self.menuQuit = ttk.Button(self.menu_window, width = self.menuButtonWidth)
        self.menuQuit.grid( row = 4, column = 1 , pady = self.padVerticalValue)

        # 2. The button configurations


        self.quitStyle = ttk.Style()
        self.quitStyle.configure("Quit.TButton", foreground = "dark red")
        self.menuQuit.config( text = "Quit" , style = "Quit.TButton" , command = lambda : self.root.quit())
        self.menu_window.pack()
    # 3. The method definitions/configurations

    def switchToNew(self,window_referance):
        self.root.withdraw()
        window_referance.deiconify()
    def switchBackMenu(self,window_referance):
        window_referance.withdraw()
        self.root.deiconify()




class FromLevelZero():
    def __init__(self, feature_title):

        self.feature_title = feature_title
        self.featureWindow = Toplevel()
    
        self.title_frame = ttk.Frame(self.featureWindow, padding = "50 10 50 0")
        self.feature1_font = font.Font( family = "System", size = 22 , weight = "bold")
        self.title_label = ttk.Label(self.title_frame, text = "From Level Zero", font = self.feature1_font, padding = "40 50 40 40")
        self.title_label.grid( row = 1 , column = 1)
        self.title_frame.pack()

        self.feature_frame = ttk.Frame(self.featureWindow, padding = "10 10 10 10")
        self.feature_frame.pack()

        self.targetLevel = StringVar()
        self.totalNeededXPNum = StringVar()
        self.inputLabel = ttk.Label(self.feature_frame, text = "Input the target level you're trying to reach: ")
        self.inputLabel.grid( row = 2 , column = 0, sticky = (E))
        self.outputLabel = ttk.Label(self.feature_frame, text = "The amount of experience needed to reach that level is: ")
        self.outputLabel.grid( row = 3, column = 0)
        self.levelEntry = ttk.Entry(self.feature_frame, width = 25 , textvariable = self.targetLevel)
        self.levelEntry.grid( row = 2 , column = 1)
        self.neededExpLabel = ttk.Label(self.feature_frame, textvariable = self.totalNeededXPNum)
        self.neededExpLabel.grid( row = 3, column = 1, sticky = (W,E))
        self.calcButton = ttk.Button(self.feature_frame, text = "Calculate!", command = self.lvlZeroCalculate)
        self.calcButton.grid( row = 4 , column = 1)
        self.backStyle = ttk.Style()
        self.backStyle.configure("Back.TButton", foreground = "systemHighlight")
        self.backButton = ttk.Button(self.feature_frame, text = "Back to Main Menu", style = "Back.TButton")
        self.backButton.grid( row = 4, column = 0 , sticky = (W,E))
      
    def lvlZeroCalculate(self):
        try:
            target = float(self.levelEntry.get())
            neededExp = 0
            if(target >= 0 and target <= 16):
                neededExp = int((target ** 2) + (target * 6))
                self.totalNeededXPNum.set(str(neededExp))
            elif(target >= 17 and target <= 31):
                neededExp = int((((target ** 2) * 2.5) - (target * 40.5)) + 360)
                self.totalNeededXPNum.set(str(neededExp))
            elif(target>= 32):
                neededExp = int((((target ** 2) * 4.5) - (target * 162.5)) + 2220)
                self.totalNeededXPNum.set(str(neededExp))
        except ValueError:
            self.totalNeededXPNum.set("Please input a correct value!")
            pass


class GrindDuration():
    def __init__ (self,feature_title):

        self.feature_title = feature_title
        self.featureWindow = Toplevel()
    
        self.title_frame = ttk.Frame(self.featureWindow, padding = "50 10 50 0")
        self.feature2_font = font.Font( family = "System", size = 22 , weight = "bold")
        self.title_label = ttk.Label(self.title_frame, text = "Grind Duration", font = self.feature2_font, padding = "40 50 40 40")
        self.title_label.grid( row = 1 , column = 1)
        self.title_frame.pack()



        self.feature_frame = ttk.Frame(self.featureWindow, padding = "20 20 20 20")
        self.feature_frame.pack()

        self.currentLVL = StringVar()
        self.targetLVL = StringVar()
        self.expGainRATE = StringVar()
        self.secondsDuration = " "
        self.minutesDuration = " "


        self.currentLvlLabel = ttk.Label(self.feature_frame, text = "Your current level is: ")
        self.currentLvlLabel.grid( row = 0 , column = 0, sticky = (E))
        self.targetLvlLabel = ttk.Label(self.feature_frame, text = "The level you're trying to reach is: ")
        self.targetLvlLabel.grid( row = 1 , column = 0, sticky = (E))
        self.expGainRateLabel = ttk.Label(self.feature_frame, text = "The amount of exp you gain per second is: ")
        self.expGainRateLabel.grid( row = 2 , column = 0, sticky = (E))
        self.currentLvlEntry = ttk.Entry(self.feature_frame, textvariable = self.currentLVL)
        self.currentLvlEntry.grid( row = 0, column = 1 )
        self.targetLvlEntry = ttk.Entry(self.feature_frame, textvariable = self.targetLVL)
        self.targetLvlEntry.grid( row = 1 , column = 1 )
        self.expGainRateEntry = ttk.Entry(self.feature_frame, textvariable = self.expGainRATE)
        self.expGainRateEntry.grid( row = 2 , column = 1 )
        self.calculateButton = ttk.Button(self.feature_frame, text = "Calculate!", width = 20 ,command = self.grindDurationCalc)
        self.calculateButton.grid( row = 3 , column = 1)
        self.fillerLabelStyle = ttk.Style()
        self.fillerLabelStyle.configure("FillerInfo.TLabel", foreground = "green4")
        self.fillerTextLabel = ttk.Label(self.feature_frame, text = "According to our calculations....", width = 70, style = "FillerInfo.TLabel")
        self.fillerTextLabel.grid( row = 4 , column = 0 )
        self.backMenuStyle = ttk.Style()
        self.backMenuStyle.configure("Back.TButton", foreground = "systemHighlight")
        self.menuBackButton = ttk.Button(self.feature_frame, text = "Back to Main Menu", width = 20, style = "Back.TButton")
        self.menuBackButton.grid( row = 5 , column = 1)

    def lvlZeroExpCalc(self, target):
        try:
            neededExp = 0
            if(target >= 0 and target <= 16):
                neededExp = int((target ** 2) + (target * 6))
                return neededExp
            elif(target >= 17 and target <= 31):
                neededExp = int((((target ** 2) * 2.5) - (target * 40.5)) + 360)
                return neededExp
            elif(target>= 32):
                neededExp = int((((target ** 2) * 4.5) - (target * 162.5)) + 2220)
                return neededExp
        except ValueError:
            #WRITE CODE TO DISPLAY A VALUE ERROR HERE LATER!!
            pass

    def grindDurationCalc(self):
        try:
            current = float(self.currentLvlEntry.get())
            target = float(self.targetLvlEntry.get())
            expRate = float(self.expGainRateEntry.get())
            expDifference = (self.lvlZeroExpCalc(target))  - (self.lvlZeroExpCalc(current))
            grossSecondsDuration = math.floor((expDifference /expRate) + 1)
            if( grossSecondsDuration > 60 ):
                grossMinutesDuration = grossSecondsDuration // 60
                fineSecondsDuration = grossSecondsDuration % 60
                if( grossMinutesDuration < 0 or grossSecondsDuration < 0):
                    raise TypeError
                self.secondsDuration = str(fineSecondsDuration)
                self.minutesDuration = str(grossMinutesDuration)
                self.fillerTextLabel.configure( text = "According to our calculations, you need to grind for " + self.minutesDuration + " minute(s) and " + self.secondsDuration + " second(s)!")
            else:
                if( grossMinutesDuration < 0 or grossSecondsDuration < 0):
                    raise TypeError
                self.secondsDuration = str(grossSecondsDuration)
                self.fillerTextLabel.configure( text = "According to our calculations, you need to grind for " + self.secondsDuration + " second(s)!")
        except ValueError:
            #Work out weird possible value bugs, such as going to negative levels
            #WRITE CODE TO DISPLAY A VALUE ERROR HERE LATER!!
            self.fillerTextLabel.configure( text = "Please input correct values!!")
            pass
        except TypeError:
            self.fillerTextLabel.configure( text = "Put in numbers that fit within the level range logically!!")
            pass




if __name__ == "__main__":

    #App initialization
    app = StartApp()
    feature1 = FromLevelZero("Calculate From Level Zero")
    feature2 = GrindDuration("Grind Duration")
    feature1.featureWindow.withdraw()
    feature2.featureWindow.withdraw()

    #Window Configurations
    app.root.title("XPCalculator")
    feature1.featureWindow.title(feature1.feature_title)
    feature2.featureWindow.title(feature2.feature_title)
    app.menuButton1.config( text = feature1.feature_title, command = lambda : app.switchToNew(feature1.featureWindow))
    app.menuButton2.config( text = feature2.feature_title, command = lambda : app.switchToNew(feature2.featureWindow))
    feature1.backButton.config( command = lambda : app.switchBackMenu(feature1.featureWindow))
    feature1.featureWindow.bind('<Return>', feature1.lvlZeroCalculate)
    feature2.menuBackButton.config( command = lambda : app.switchBackMenu(feature2.featureWindow))

    #Start of the app
    app.root.mainloop()


    #print(font.families())  
    # ^^^^^^^ Use this if you want to print the font familes th are stored on your computer
   
    
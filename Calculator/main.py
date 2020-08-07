from tkinter import *
from tkinter import ttk
from tkinter import font
import time
import math
from PIL import ImageTk, Image



class StartApp():
    def __init__(self):

        # 1. All the window and button definitions
        self.root = Tk()
        self.menu_window = ttk.Frame(self.root, padding = "100 10 100 10")
        
        # - Code for placing the Application Title Image
        self.raw_title_image = Image.open('C:/Users/Anthony/workspace/code_workspace/Python/XPCalculator/Images&Media/Title_Image.png')
        self.zoom = 0.25
        pixels_x, pixels_y = tuple([int(self.zoom * x)  for x in self.raw_title_image.size])
        self.title_image = ImageTk.PhotoImage(self.raw_title_image.resize(( pixels_x , pixels_y)))
        self.title_label = ttk.Label(self.menu_window,  image = self.title_image)
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
        self.featureWindow.bind('<Return>' , self.lvlZeroCalculate)

    
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
        self.calcButton = ttk.Button(self.feature_frame, text = "Calculate!", command = self.lvlZeroCalculate, width = 25)
        self.calcButton.grid( row = 4 , column = 1)
        self.backStyle = ttk.Style()
        self.backStyle.configure("Back.TButton", foreground = "systemHighlight")
        self.backButton = ttk.Button(self.feature_frame, text = "Back to Main Menu", style = "Back.TButton")
        self.backButton.grid( row = 4, column = 0 , sticky = (W,E))


    def resetEntries(self):
        self.targetLevel = " "
        self.totalNeededXPNum = " "
      
    def lvlZeroCalculate(self, event = None):
        try:
            target = float(self.levelEntry.get())
            if( target < 0):
                raise ValueError
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
        self.featureWindow.bind('<Return>', self.grindDurationCalc)
    
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
        self.SecondS = ""
        self.MinuteS = ""


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
        self.calcButton = ttk.Button(self.feature_frame, text = "Calculate!", width = 20 ,command = self.grindDurationCalc)
        self.calcButton.grid( row = 3 , column = 1)
        self.fillerLabelStyle = ttk.Style()
        self.fillerLabelStyle.configure("FillerInfo.TLabel", foreground = "green4")
        self.fillerTextLabel = ttk.Label(self.feature_frame, text = "According to our calculations....", width = 80, style = "FillerInfo.TLabel")
        self.fillerTextLabel.grid( row = 4 , column = 0 )
        self.backMenuStyle = ttk.Style()
        self.backMenuStyle.configure("Back.TButton", foreground = "systemHighlight")
        self.backButton = ttk.Button(self.feature_frame, text = "Back to Main Menu", width = 20, style = "Back.TButton")
        self.backButton.grid( row = 5 , column = 1)

    def resetEntries(self):
        self.currentLVL = " "
        self.targetLVL = " "
        self.expGainRATE = " "
        self.fillerTextLabel.config( text = "According to our calculations....")

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
            pass

    def grindDurationCalc(self, event = None):
        try:
            self.SecondS = ""
            self.MinuteS = ""
            current = float(self.currentLvlEntry.get())
            target = float(self.targetLvlEntry.get())
            expRate = float(self.expGainRateEntry.get())
            if( current < 0 or target < 0 or expRate < 0 or target < current):
                raise TypeError
            expDifference = (self.lvlZeroExpCalc(target))  - (self.lvlZeroExpCalc(current))
            grossSecondsDuration = math.floor((expDifference /expRate) + 1)
            if( grossSecondsDuration > 60 ):
                grossMinutesDuration = grossSecondsDuration // 60
                fineSecondsDuration = grossSecondsDuration % 60
                if(fineSecondsDuration > 1):
                    self.SecondS = "s"
                if(grossMinutesDuration > 1):
                    self.MinuteS = "s"
                self.secondsDuration = str(fineSecondsDuration)
                self.minutesDuration = str(grossMinutesDuration)
                self.fillerTextLabel.configure( text = "According to our calculations, you need to grind for " + self.minutesDuration + " minute{0} and ".format(self.MinuteS) + self.secondsDuration + " second{0}!".format(self.SecondS))
            else:
                if( grossSecondsDuration > 1 ):
                    self.SecondS = "s" 
                self.secondsDuration = str(grossSecondsDuration)
                self.fillerTextLabel.configure( text = "According to our calculations, you need to grind for " + self.secondsDuration + " second{0}!".format(self.SecondS))
        except ValueError:
            self.fillerTextLabel.configure( text = "Please input correct numerical values!!")
            pass
        except TypeError:
            self.fillerTextLabel.configure( text = "Put in numbers that fit within the level range logically!!")
            pass

class BottleCounter():
    def __init__(self, feature_title):
        self.feature_title = feature_title
        self.featureWindow = Toplevel()
        self.featureWindow.bind('<Return>', self.allCalc)

        self.title_frame = ttk.Frame(self.featureWindow, padding = "50 10 50 0")
        self.feature3_font = font.Font( family = "System", size = 22 , weight = "bold")
        self.title_label = ttk.Label(self.title_frame, text = "XP Bottle Counter", font = self.feature3_font, padding = "40 50 40 40")
        self.title_label.grid( row = 1 , column = 1)
        self.title_frame.pack()
        bottleOfEnchantingGIF = Image.open('C:/Users/Anthony/workspace/code_workspace/Python/XPCalculator/Images&Media/Bottle_Of_EnchantingGIF.gif')
        self.title_image = ImageTk.PhotoImage(bottleOfEnchantingGIF)
        self.image_label = Label(self.featureWindow, image = self.title_image)
        self.image_label.pack()

        self.feature_frame = ttk.Frame(self.featureWindow, padding = "20 20 20 20")
        self.feature_frame.pack()

        self.currentLVL = StringVar()
        self.targetLVL = StringVar()
        self.exceptionOutput = " "
        self.maximumAmountNum = StringVar()
        self.averageAmountNum = StringVar()
        self.minimumAmountNum = StringVar()

        self.currentLevelLabel = ttk.Label(self.feature_frame, text = "Your current level is: ")
        self.currentLevelLabel.grid( row = 0 , column = 0, sticky = (E))
        self.currentLevelEntry = ttk.Entry(self.feature_frame, textvariable = self.currentLVL)
        self.currentLevelEntry.grid( row = 0, column = 1)
        self.targetLevelLabel = ttk.Label(self.feature_frame, text = "The level you are trying to reach is: ")
        self.targetLevelLabel.grid( row = 1 , column = 0, sticky = (E))
        self.targetLevelEntry = ttk.Entry(self.feature_frame, textvariable = self.targetLVL)
        self.targetLevelEntry.grid( row = 1 , column = 1)
        self.exceptionStyle = ttk.Style()
        self.exceptionStyle.configure("ExceptStyle.TLabel", foreground = "gold2")
        self.exceptionErrorLabel = ttk.Label(self.feature_frame, style = "ExceptStyle.TLabel")
        self.exceptionErrorLabel.grid( row = 2, column = 0)
        self.calcButton = ttk.Button(self.feature_frame, text = "Calculate!", width = 20, command = self.allCalc)
        self.calcButton.grid( row = 2, column = 1)
        self.maximumAmountLabel = ttk.Label(self.feature_frame, text = "The Maximum Amount of bottles needed is: ")
        self.maximumAmountLabel.grid( row = 3, column = 0, sticky = (E) )
        self.averageAmountLabel = ttk.Label(self.feature_frame, text = "The Average Amount of bottles needed is: ")
        self.averageAmountLabel.grid( row = 4, column = 0, sticky = (E) )
        self.minimumAmountLabel = ttk.Label(self.feature_frame, text = "The Minimum Amount of bottles needed is: ")
        self.minimumAmountLabel.grid( row = 5, column = 0, sticky = (E) )
        self.maximumAmountOutput = ttk.Label(self.feature_frame, textvariable = self.maximumAmountNum)
        self.maximumAmountOutput.grid( row = 3, column = 1)
        self.averageAmountOutput = ttk.Label(self.feature_frame, textvariable = self.averageAmountNum)
        self.averageAmountOutput.grid( row = 4, column = 1)
        self.minimumAmountOutput = ttk.Label(self.feature_frame, textvariable = self.minimumAmountNum)
        self.minimumAmountOutput.grid( row = 5, column = 1)
        self.backMenuStyle = ttk.Style()
        self.backMenuStyle.configure("BackStyle.TButton", foreground = "systemHighlight" )
        self.backButton = ttk.Button(self.feature_frame, text = "Back to Main Menu", style = "BackStyle.TButton", width = 40)
        self.backButton.grid( row = 6, column = 0)
        
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
            pass
    
    def MinimumCalc(self):
        try:
            target = float(self.targetLVL.get())
            current = float(self.currentLVL.get())
            expDiff = (self.lvlZeroExpCalc(target)) - (self.lvlZeroExpCalc(current))
            if ( target < 0 or current < 0 or expDiff < 0 ):
                raise TypeError
            minimumBottles = math.floor((expDiff / 11) + 1)
            self.minimumAmountNum.set(str(minimumBottles))
            self.exceptionOutput = " "
            self.exceptionErrorLabel.configure( text = self.exceptionOutput)
        except ValueError:
            self.minimumAmountNum.set(" ")
            self.exceptionOutput = "Please input correct values!!"
            self.exceptionErrorLabel.configure( text = self.exceptionOutput)
        except TypeError:
            self.minimumAmountNum.set(" ")
            self.exceptionOutput = "Please input logical values within range!!"
            self.exceptionErrorLabel.configure( text = self.exceptionOutput)

    def AverageCalc(self):
        try:
            target = float(self.targetLVL.get())
            current = float(self.currentLVL.get())
            expDiff = (self.lvlZeroExpCalc(target)) - (self.lvlZeroExpCalc(current))
            if ( target < 0 or current < 0 or expDiff < 0 ):
                raise TypeError
            averageBottles = math.floor((expDiff / 7) + 1)
            self.averageAmountNum.set(str(averageBottles))
            self.exceptionOutput = " "
            self.exceptionErrorLabel.configure( text = self.exceptionOutput)
        except ValueError:
            self.averageAmountNum.set(" ")
        except TypeError:
            self.averageAmountNum.set(" ")
    
    def MaximumCalc(self):
        try:
            target = float(self.targetLVL.get())
            current = float(self.currentLVL.get())
            expDiff = (self.lvlZeroExpCalc(target)) - (self.lvlZeroExpCalc(current))
            if ( target < 0 or current < 0 or expDiff < 0 ):
                raise TypeError
            maximumBottles = math.floor((expDiff / 3) + 1)
            self.maximumAmountNum.set(str(maximumBottles))
            self.exceptionOutput = " "
            self.exceptionErrorLabel.configure( text = self.exceptionOutput)
        except ValueError:
            self.maximumAmountNum.set(" ")
        except TypeError:
            self.maximumAmountNum.set(" ")

    def allCalc(self, event = None):
        self.MinimumCalc()
        self.AverageCalc()
        self.MaximumCalc()
    
    def resetEntries(self):
        self.currentLVL.set(" ")
        self.targetLVL.set(" ")
        self.exceptionOutput = " "
        self.exceptionErrorLabel.configure( text = self.exceptionOutput)
        self.minimumAmountNum.set(" ")
        self.averageAmountNum.set(" ")
        self.maximumAmountNum.set(" ")
        


if (__name__ == "__main__"):

    #App initialization
    app = StartApp()
    feature1 = FromLevelZero("Calculate From Level Zero")
    feature2 = GrindDuration("Grind Duration")
    feature3 = BottleCounter("XP Bottle Counter")
    feature1.featureWindow.withdraw()
    feature2.featureWindow.withdraw()
    feature3.featureWindow.withdraw()

    def switchBackAndClear(featureObject):
        app.switchBackMenu(featureObject.featureWindow)
        featureObject.resetEntries()

    #Window Configurations
    app.root.title("XPCalculator")
    feature1.featureWindow.title(feature1.feature_title)
    feature2.featureWindow.title(feature2.feature_title)
    feature3.featureWindow.title(feature3.feature_title)
    app.menuButton1.config( text = feature1.feature_title, command = lambda : app.switchToNew(feature1.featureWindow))
    app.menuButton2.config( text = feature2.feature_title, command = lambda : app.switchToNew(feature2.featureWindow))
    app.menuButton3.config( text = feature3.feature_title, command = lambda : app.switchToNew(feature3.featureWindow))
    feature1.backButton.config( command = lambda : switchBackAndClear(feature1))
    feature2.backButton.config( command = lambda : switchBackAndClear(feature2))
    feature3.backButton.config( command = lambda : switchBackAndClear(feature3))
    
    #Start of the app
    app.root.mainloop()
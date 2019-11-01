from graphics import *
from calc_functions import *

class Display:
    def __init__(self,win):
        self.win = win
        self.ansdisplay = Text(Point(250,50), "")
    def draw(self,win):
       self.ansdisplay.draw(win)
    def getText(self):
        return self.ansdisplay.getText()
    def setText(self,text):
        return self.ansdisplay.setText(text)

def createCanvas():
    win = GraphWin("Calculator",400, 600)
    win.setBackground("navy")

    inputdisplay = Rectangle(Point(5,5),Point(395,100))
    inputdisplay.setFill("white")
    inputdisplay.draw(win)
    return win

class Button:
    def __init__(self,coords,label,size,win):
        print(coords)
        self.size = size
        self.label = label
        self.position = Point(coords[0],coords[1])
        self.color = "lightblue"
        p=self.position
        self.rectangle = Rectangle(Point(p.getX()+self.size,p.getY()+self.size)
                                 ,Point(p.getX(),p.getY()))
        self.label = Text(Point(p.getX()+ size/2, p.getY() + size/2),label)
        self.rectangle.setFill(self.color)
        self.rectangle.draw(win)
        self.label.draw(win)
    def buttonclick(self,coords):
        for i in range(23):
            x,y = coords(i)
            if x <= click.getX() <= x + 60 and y <= click.getY() <= y+60 :
                print("i",i)
                return getLabel(i)
            return ""


    def getLabel(self):
            return self.label

class Keypad:
    def  __init__(self,win):
        self.buttons = self.createButtons(win)
    def createButtons(self,win):
        coords = [[50,150],[120,150],[190,150],[260,150],
            [50,220],[120,220],[190,220],[260,220],
            [50,290],[120,290],[190,290],[260,290],
            [50,360],[120,360],[190,360],[260,360],
            [50,430],[120,430],[190,430],[260,430],
            [50,500],[120,500],[190,500]]

        labels = ['7','6','5','4',
            '3','2','1','0',
             '-','+','=','/',
            '*','+/-','C','.',    
            '8','9',"M+","M-",
            "MR","MC","Del" ]
        buttons = []
        for i in range(len(coords)):
            button = Button(coords[i],labels[i],50,win)
            buttons.append(button)
        return buttons
    
##def createButtons(win):
##    #creates button display
##    color = ['lightblue','lightblue','lightblue','lightblue'
##             ,'lightblue','lightblue','lightblue','lightblue'
##             ,'lightblue','lightblue','lightblue','lightblue'
##             ,'lightblue','lightblue','lightblue','lightblue'
##             ,'lightblue','lightblue','lightblue','lightblue'
##             ,'lightblue','lightblue','lightblue','lightblue',
##             'lightblue','lightblue','lightblue']
##    size = [60,60]
##    #creates button shape
##    for i in range(23):
##        x,y = getCoords(i)
##        
##        button = Rectangle(Point(x,y),Point(x+size[0],y+size[1]))
##        button.setFill(color[i])
##        button.draw(win)
##        label = Text(Point(x+30,y+30),getLabel(i))
##        label.draw(win)
##       
##    
##
##def getCoords(i):
##    coords = [[50,150],[120,150],[190,150],[260,150],
##              [50,220],[120,220],[190,220],[260,220],
##              [50,290],[120,290],[190,290],[260,290],
##              [50,360],[120,360],[190,360],[260,360],
##              [50,430],[120,430],[190,430],[260,430],
##              [50,500],[120,500],[190,500]]
##    return coords[i][0],coords[i][1]
##
##def getLabel(i):
##    labels = ['7','6','5','4',
##              '3','2','1','0',
##              '-','+','=','/',
##              '*','+/-','C','.',    
##              '8','9',"M+","M-",
##              "MR","MC","Del"]
##    return labels[i]
    
##def buttonclick(click):
##    for i in range(23):
##        x,y = coords(i)
##        if x <= click.getX() <= x + 60 and y <= click.getY() <= y+60 :
##            print("i",i)
##            return getLabel(i)
##    return ""

def operations(probStr):
    opList = probStr.split()
    if "-" in opList[len(opList)-1]:
        minusIndex = opList[len(opList)-1].index("-")
        opList[len(opList)-1] = opList[len(opList)-1][minusIndex+1:]

    else:
            opList[len(opList)-1] = "-" + opList[len(opList)-1]

    return " ".join(opList)

def getResult():
   total = Calc(inputstring)
   return inputstring + " = " + total

#def setMemory(operations,value,memory):
    #if operations == "M+":
        #return memory + value
    #elif operations == "M-":
        
    
    
def main():
    win = createCanvas()
    display = Display(win)
    display.draw(win)
    probStr = ""
    memory = 0
    keypad = Keypad(win)
    
    while True:
            click = win.getMouse()
            inputstring = Button.buttonclick
            probStr = display.getText()
            print("in",inputstring)
            
            if inputstring == "Del":
                probStr = ""
                display.setText(probStr)
            elif inputstring == ".":
                display(win).setText(display.getText()+ ".")
            elif inputstring == "+/-":
                probStr = operations(probStr)
                display.setText(probStr)
            elif inputstring == "/" or inputstring == "x" or inputstring == "+" or inputstring == "-":
                probStr += " " + inputstring + " "
                display.setText(probStr)
            elif inputstring == "=":
                result = Calc(probStr.split())
                display.setText(result)
                probStr = result
            elif inputstring == "M+":
                memory = memory + float(Calc(probStr.split()))
                probStr = str(memory)
                display.setText(result)
            elif inputstring == "M-":
                memory = memory - float(Calc(probStr.split()))
                probStr = str(memory)
            elif inputstring == "MR":
                probStr = probStr + str(memory)
            elif inputstring == "MC":
                memory = 0
            elif inputstring == "C":
                memory = 0
                probStr = ""
            
            else:
                print("prob",probStr)
                print(inputstring)
                probStr += inputstring
                display.setText(probStr)
            print("prob",probStr)
            display.setText(probStr)
        
main()

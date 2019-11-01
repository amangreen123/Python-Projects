from calc_functions import *
from graphics import *



def drawBackground():
    win = GraphWin("Calculator",400, 600)
    win.setBackground("#fdfd96")

    p1 = Point(40,18)
    p2 = Point(350,80)
    screen = Rectangle(p1,p2)
    screen.setFill("#DCDCDC")
    screen.draw(win)
    return win
 
def createDisplay(win):
    display = Text(Point(250,50), "")
    display.draw(win)
    return display

def getCoords(index):
    coords = [[50,150],[120,150],[190,150],[260,150],[50,220],[120,220],[190,220],[260,220],[50,290],[120,290],[190,290],[260,290],[50,360],[120,360],[190,360],[260,360],[190,430],[260,430]]
    return coords[index][0],coords[index][1]

def getLabel(index):
    labels = ["7","8","9","/","4","5","6","x","1","2","3","+","+/-","0",".","-","Del","="]
    return labels[index]

def getButton(point):
    for i in range(18):
        x,y = getCoords(i)
        if x <= point.getX() <= x + 60 and y <= point.getY() <= y+60 :
            return getLabel(i)


def plusMinus(numStr):
    eqList = numStr.split()
    if "-" in eqList[len(eqList)-1]:
        minusIndex = eqList[len(eqList)-1].index("-")
        eqList[len(eqList)-1] = eqList[len(eqList)-1][minusIndex+1:]
    else:
        eqList[len(eqList)-1] = "-" + eqList[len(eqList)-1]
                            
    return " ".join(eqList)


def drawButtons(win):
    
    color = ["lightblue","lightblue","lightblue","orange","lightblue","lightblue","lightblue","orange","lightblue","lightblue","lightblue","orange","orange","lightblue","lightblue","orange","orange","orange"]
    size = [60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60]

    for i in range (18):
        x,y = getCoords(i)
        button = Rectangle(Point(x,y),Point(x+size[i],y+size[i]))
        button.setFill(color[i])
        label = Text(Point(x+size[i]/2,y+size[i]/2),getLabel(i))
        button.draw(win)
        label.draw(win)
        
def main():
    win = drawBackground()
    drawButtons(win)
    display = createDisplay(win)
    eqStr = ""

    try:
        while True:
            point = win.getMouse()
            button = getButton(point)
            eqStr = display.getText()

            if button == "Del":
                eqStr == ""
                display.setText("")
            elif button == ".":
                display.setText(display.getText()+ ".")
            elif button == "+/-":
                eqStr = plusMinus(eqStr)
                display.setText(eqStr)
            elif button == "/" or button == "x" or button == "+" or button == "-":
                display.setText(display.getText()+ " " + button + " ")
            elif button == "=":
                display.setText(run(eqStr))
                eqStr == ""
            elif str(button) == "None":
                display.setText(display.getText())
            else:
                display.setText(display.getText() + button)
    except TypeError:
            display.setText("Invalid input")
    except GraphicsError:
        print("Calculator closed")
        

main()

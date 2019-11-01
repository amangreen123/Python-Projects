# 3 + 4 * 5 – 3 / 4

def main():
    # holds the equation in the list
    equation = (list(input("Enter Your equation with no spaces: ")))
 
    equation = conc(equation)
    print(equation)
    final = Calc(equation)
    print("answer is:",final)


def conc(equation = []):
    finalEqu = []
    count = 0
    num = ""

    for i in range(len(equation)):
        if (equation[i] == '+' or equation[i] == '-' or equation[i] == '*' or equation[i] == '/'):

            num =  equation[i-count:i]
            newnum = "".join(num)
            finalEqu.append(newnum)
            finalEqu.append(equation[i])
            count = 0
            num = ""

        elif (len(equation) == i + 1):
            
            num = equation[i-count:i+1]
            newnum = "".join(num)
            finalEqu.append(newnum)
            count = 0
            num = ""
            
        else:
            count = count + 1
            
    return finalEqu

def Calc(equation=[]):
    while(len(equation) != 1):
       #pemdas 
        while(("*" in equation) or ("/" in equation)):

            for i in range(1, len(equation)):
               #multiply
                if((equation[i]=="*") or (equation[i]=="/")):
                    if(equation[i]=="*"):
                        product = multi(float(equation[i-1]),float(equation[i+1]))
                        product = str(product)
                        equation = insert(product,i,equation)
                        break
                #division
                    elif(equation[i]=="/"):
                        quotient = divi(float(equation[i-1]),float(equation[i+1]))
                        quotient = str(quotient)
                        equation = insert(quotient,i,equation)
                        break
                    break

        for i in range(1, len(equation)):
            
            if((equation[i]=="+") or (equation[i]=="-")):

                   #addition
                    if(equation[i]=="+"):
                        Sum = add(float(equation[i-1]),float(equation[i+1]))
                        Sum = str(Sum)
                        equation = insert(Sum,i,equation)
                        break
                  #subtraction
                    if(equation[i]=="-"):
                        subtract = sub(float(equation[i-1]),float(equation[i+1]))
                        subtract = str(subtract)
                        equation = insert(subtract,i,equation)
                        break
                    break

            
    finalEquation = equation[0]
    return finalEquation

def insert(finalNumber, i, equation = []):
    del equation[i-1:i+2]
    equation.insert(i-1,finalNumber)
    print(equation)
    return equation 

def sub(x,y):
    return x-y

def add(x,y):
    return x+y

def multi(x,y):
    return x*y

def divi(x,y):
    return x/y

        

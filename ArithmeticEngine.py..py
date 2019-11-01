def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def showOutro():
    print("\nThank you for using the Arithmetic Engine…")
    print("\nPlease come back again soon!")

def doLoop():
    while True:
        cmd = input("What computation do you want to perform? ").lower()
        if cmd in ['add','sub','mult','div']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if cmd == "add":
                result = num1 + num2
            elif cmd == "sub":
                result = num1 - num2
            elif cmd == "mult":
                result = num1 * num2
            elif cmd == "div":
                try:
            
                    result = num1 / num2
                except:
                    print("cant divide by zero")
                    continue
            elif cmd == "quit":
                exit()
            print("The result is " + str(result) + ".\n")
        else:
            print("Error enter valid command")
            

def main():
    showIntro()
    doLoop()
    showOutro()

main()

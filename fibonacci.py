
def main():

    n = int(input("Enter the value of n: "))
    a,b = 1,1
    for i in range(n-2):
        a,b = a+b, a

        print("The nth Fibonacci number is",a)

main()
        

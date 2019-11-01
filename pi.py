#pi.py


import math

def main ():
   

    n = int(input("How many terms should I use?"))

    amount = 0.0
    si = 1.0

    for p in range (1,2*n,2):
        amount = amount + si * 4.0/p
        si = -si #flips the sign

        print("Approximation to pi is:", amount)
        print("Difference from math.pi:", math.pi - amount)

main()

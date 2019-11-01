# areafunctions.py

import math

def sphereArea(radius):
    return 4 * radius * radius * math.pi

def sphereVolume(radius):
    return 4 / 3 * math.pi * radius ** 3

def main():
    radius = 30
    print(sphereArea(radius))
    print(sphereVolume(radius))

main()

# Pythagoras Theorem Calculator

import math

def Pythagoras(width,height):
    print('The width is:', width**2)
    print('The height is :',height**2)

    return math.sqrt(width**2 + height**2)

numbers = input('Please enter the width and height of the triangle separated by a comma: ')


width, height = numbers.split(',')
print(width, height)


print('The length of the hypothenuse is: ', Pythagoras(int(width),int(height)))
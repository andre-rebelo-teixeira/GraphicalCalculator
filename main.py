import math
from click import confirm 
import numpy 
#import pygame 


''' Basic math functions '''
def add(number, number1):
    return number + number1

def subtract(number, number1):
    return number - number1

def division(number, number1):
    return number / number1

def multiplication(number, number1):
    return number * number1

def exponential(base, expoent):
    return base ** expoent

def log(base, number): 
    return log(number, base )

''' String analysis function'''
def analysys(string):
    string.split('(' ')')

def confirmString(string):
    number1, number2 = 0, 0
    for char in string:
        if (char == "("):
            number1 += 1
        elif(char == ")"):
            number2 += 1

    if (number1 != number2):
        return True
    else:
        return False

        
#comentario

def main():
    string = "((4+2)+3)"
    
    if (confirmString(string)):
        return

    string = string.replace('(', '[')
    string = string.replace(')', ']')



    print(string)

'''safety check'''
if __name__ == "__main__":
    main()




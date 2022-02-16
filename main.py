from itertools import count
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

        
'''
A função interpreter basicamente é responsavel por separar a string pelos parentises e calcular o valor dentro deles
com recurso à função evaluate.
Isto é basicamente uma função recursiva que vai correr pela string, e sempre que encontra um fechar parentises e calcula
o valor entre esse mesmo parentises e o seu correpondente.
Caso existam parentises dentro desta string, esta é enviada de novo para a função interpreter
'''
def interpreter(string):

    index=[]                                                                    #iniciar as variaveis
    counter=0

    for char in string:                                                         #fazer um for loop para correr pelos caracteres

        if char=='(':                                                           #se encontrar uma abertura de parentises, adicionar o valor
            index.append(counter+1)                                             #do indice à lista

        if char==')':                                                           #se encontrar um fecho de parentises, calcular o valor

            string_piece_by_brackets=string[index[-1]: counter]                 #isolar a parte da string a calcular
            #print(string_piece_by_brackets)

            result = interpreter(string_piece_by_brackets)                      #realizar a separação de parentises

            counter=counter-len(string[index[-1]: counter])+len(result)-2       #adequar o counter ao novo numero de char
            string=string.replace('(' + string_piece_by_brackets + ')', result) #fazer replace do valor calculado na string original
            index=index[0:-1]                                                   #retirar o ultimo valor registado na lista index

        #print(string, char, index, counter)

        counter = counter+1                                                     #adicionar um valor ao count

    return str(eval(string))



def evaluate(string):

    if any(i in '**' for i in string) or any(i in '^' for i in string):
        counter=0
        for char in string:
            if ~(char.isdigit) and char!='.' and char!='e':
                print()


    if any(i in '*' for i in string) or any(i in '/' for i in string):
        counter=0
        for char in string:
            print()









def main():
    string = "((4/3)+3**50-(5+2))"
    
    if (confirmString(string)):
        return

    result = interpreter(string)

    print(result)


    #print(string)

'''safety check'''
if __name__ == "__main__":
    main()




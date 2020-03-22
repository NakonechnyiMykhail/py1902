# v1
# import math
# print(math.pi)
# print(math.cos(0.5))
# v2
# import math as m
# print(m.pi)
# print(m.cos(0.5))

# v3
# from math import e, sin, cos, pi
# print(pi)
# print(cos(0.5))

# v4
# from math import *
# print(pi)
# print(cos(0.5))




from random import randint

def getRandomNumber():
    return randint(0,50)

def avarage(numbers):
    summa = 0
    for index in numbers:
        summa += index
    # print(summa/len(numbers))
    return summa/len(numbers)

def summa(numbers):
    summa = 0
    for index in numbers:
        summa += index
    # print(summa)
    return summa

def summa2(numbers):
    summa = 0
    for index in numbers:
        if index%2==0:
            summa += index
    # print(summa)
    return summa
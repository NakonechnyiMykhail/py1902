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


numbers = []
for index in range(0,10):
    numbers.append(getRandomNumber())
    print(numbers[index])

# print('index 3 = ', numbers[3])

print('Avarage  = ', avarage(numbers))
print('Summa    = ', summa(numbers))
print('Summa2   = ', summa2(numbers))
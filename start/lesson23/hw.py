#import random
from random import randint

def get_random_number(startNumber, endNumber):
    # random function
    return randint(startNumber, endNumber)

def hello():
    name = input('Enter your name: ')
    print('Hello, ', name)
    age = input('Enter your age: ')
    print('Your age is ', age)
    person = [name, age]
    return person

def transform(liste):
    first = len(liste[0])*3
    end = int(int(liste[1])*17/6)
    #print(end)
    numbers = [first, end]
    return numbers


man = hello()
randoms = transform(man)
#print(transform(man))
# print(man)
# print(man.values())
# print(man.keys())

#numbers = [0,2,4,2,1]
numbers = []
for index in range(10):
    numbers.append(get_random_number(randoms[0],randoms[1]))
    print(numbers[index])


#1
#print(get_random_number(0,10))
#2
#randomNumber = get_random_number(0,10)
#print(randomNumber)
#print(randomNumber)
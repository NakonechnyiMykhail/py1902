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
    person = {'name':name,'age':age}
    return person

def transform(dictionary):
    first = len(dictionary['name'])*3
    end = int(int(dictionary['age'])*17/6)
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
    # print(numbers[index])

print(numbers)
# a = numbers.append(78)
# b = numbers.pop(1)
# c = numbers.sort()
# d = numbers.reverse()
# print(a)
# print(b)
# print(c)
# print(d)



#1
#print(get_random_number(0,10))
#2
#randomNumber = get_random_number(0,10)
#print(randomNumber)
#print(randomNumber)
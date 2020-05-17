# v1

# task1 project
# author: Mikhail
# version: 1.0
# date: 10/05/2020

# description ...... some text ......

# v2
"""
task1 project
author: Mikhail
version: 1.0
date: 10/05/2020

description ...... some text ......
"""


text = """
создать класс               : MyClass
создать внутри переменную   : number = 10
создать внутри функцию      : hello -> print('hello')
___________________________________________

вывести переменную
вывести функцию
"""
#'' / ""
# print(text)

class WelcomeClass:
    """
    ___________________________________________
    создать класс               : MyClass
    создать внутри переменную   : number = 10
    создать внутри функцию      : hello -> print('hello')
    ___________________________________________
    """

    number = 10

    def hello(self):
        #print('hello')
        return 'hello'


# cl = WelcomeClass()
#print(number)      #-> 10
#print(cl.number)    #-> 10


# print(WelcomeClass.number)
# print(cl.hello())
print(WelcomeClass.__doc__)
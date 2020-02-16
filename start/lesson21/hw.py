def getName(): # get_name()
    name = input('Enter your name: ')
    print('Hello, ' + name)
    return name

def getAge(): # get_age()
    age = int(input('Enter your age: '))
    return age

def check(var1, var2):
    mult = len(var1)*var2
    summ = len(var1)+var2
    # print(mult)
    # print(summ)
    if (mult>30 and mult<40):
        for index in var1:
            print(index)
    elif mult>40:
        print(var1*3)
    elif summ<20:
        print(var1.upper())
    else:
        for index in range(0, summ, 4):
            print(index)

check(getName(), getAge())

# for index in 'Mike':
#     print(index)

# for index in range(0,10,2):
#     print(index)



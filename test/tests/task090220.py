def getName():
    name = input('your name> ')
    print('Hi,' + name)
    return name

def age():
    age = input('how old are you > ')
    return age


def check(name,age):
    a = len(name) * age
    print(a)
    if (a > 30 and a < 40):
        for index in name:
            print(index)
    elif a > 40:
        print(name*3)
    elif len(name)+age < 20:
        print(name.upper())
    else:
        print(len(name) + age)




a = int(age())
n = getName()
check(n,a)
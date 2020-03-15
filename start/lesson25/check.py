def get_age():
    age = int(input('Enter your age: '))
    return age

def check_1(age):
    if age < 3:
        return 'baby'
    elif age >= 3 and age < 18:
        return 'teenager'
    elif age >=18 and age < 60:
        return 'middle'
    elif age >=60 and age < 140:
        return 'citizen'
    else:
        return 'you\'re GOD!'

def check_2(age):
    typ = None
    if age < 3:
        typ = 'baby'
    elif age >= 3 and age < 18:
        typ = 'teenager'
    elif age >=18 and age < 60:
        typ = 'middle'
    elif age >=60 and age < 140:
        typ = 'citizen'
    else:
        typ = 'you\'re GOD!'
    return typ

def check_3(age):
    typ = None
    if age < 3:
        typ = 'baby'
    elif age >= 3 and age < 18:
        typ = 'teenager'
    elif age >=18 and age < 60:
        typ = 'middle'
    elif age >=60 and age < 140:
        typ = 'citizen'
    else:
        typ = 'you\'re GOD!'
    print(typ)
#1
print(check_1(get_age()))

#2
print(check_2(get_age()))

#3
check_3(get_age())
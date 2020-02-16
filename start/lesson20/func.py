# def hello():
#     print('hello')

def get_name():
    name = input('enter your name: ')
    return name

def hello(name):
    print('hello, ' + name)

def loop(name):
    for index in name:
        print(index)


# hello(get_name())
loop(get_name())


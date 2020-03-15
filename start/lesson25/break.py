name = None
while True:
    print('Menu:')
    print('1. Set name')
    print('2. Print hello')
    print('3. Exit')
    response = input('Enter menu number: ')
    print()
    if response == '1':
        name = input('Enter your name: ')
    elif response == '2':
        if name:
            print('Hello, ', name, '!', sep='')
        else:
            print('I don\'t know your name.' )
    elif response == '3':
        break
    else:
        print('Uncorrect input!')

    print()
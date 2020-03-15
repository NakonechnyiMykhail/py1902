x = 3
while x:
    x -= 1 # x = x - 1
    response = input('Enter \'stop\' to stop the application')
    if response == 'stop':
        break
    else:
        print('loop was ended by itself')

print('Program end.')
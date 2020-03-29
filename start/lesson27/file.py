with open('newfile.txt', 'w', encoding='utf-8') as f:
    d = int(input('Enter the numbers : '))
    print('1 / {} = {}'.format(d, 1 / d), file = f)
# import fun
#1
# print(100/0)
# output = ZeroDivisionError: division by zero

#2
# print(2 + '1')
# output = TypeError: unsupported operand type(s) for +: 'int' and 'str'

#3
# print(int('qwerty'))
# output = ValueError: invalid literal for int() with base 10: 'qwerty'

#4
# try:
#     value = 1 / 0
# except ZeroDivisionError:
#     value = 0
#5
# try:
#     value = 1 / 0
# except ArithmeticError:
#     value = 0

# print(value)

f = open('data1.txt')
numbers = []
summ = 0

# for line in f:
#     numbers.append(int(line))

# for index in numbers:
#     summ += index
# print(summ)

# f.close()
# print('File is closed.')

try:
    for line in f:
        numbers.append(int(line))

    for index in numbers:
        summ += index
    print(summ)
except ValueError:
    print('Это не число. Выход')
except Exception:
    print('Это что такое?')
else:
    print('OK')
finally:
    f.close()
    print('File is closed.')

print('smth')
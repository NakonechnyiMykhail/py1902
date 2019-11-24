# логические операции

print('and:')
print(False and False)
print(False and True)
print(True and False)
print(True and True)
print()

print('or:')
print(False or False)
print(False or True)
print(True or False)
print(True or True)
print()

print('not:')
print(not False)
print(not True)
print()


# логические выражения

a = True
b = False
c = True
f = a and not b or c or (a and (b or c))
print(f)


# #####################################
a = 3
b = a
a = a - 1
print(a, b)
print(a < b)       # меньше
print(b > 3)       # больше
print(a <= 2)      # меньше или равно
print(b >= 7)      # больше или равно
print(a < 3 < b)   # двойное сравнение
print(a == b)      # равенство
print(a != b)      # неравенство
print(a is b)      # идентичность объектов в памяти
print(a is not b)  # a и b – разные объекты (хотя значения их могуть быть равны)

string = "some string"
second_string = string
third_string = input('Введите строку: ')
print(string is second_string)
print(string is third_string)

# x = int(input('Enter the card: ')) #37000
#  r = int(x / 1000)
# (r >= 37 and r <= 42) or (r >= 5500 and r < 6000)

print()
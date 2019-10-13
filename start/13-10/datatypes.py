# числа в десятичной системе счисления
dec1 = 8
dec2 = 42
dec3 = -3
dec4 = 25802836572356723058203845293402834028304820938402834023580235777082489436236


print(dec1)
print(dec2)
print(dec3)
print(dec4)
print()

# числа в шестнадцатеричной системе счисления
hex1 = 0x9
hex2 = 0xA
hex3 = 0xFF
hex4 = 0x3de

print(hex1)
print(hex2)
print(hex3)
print(hex4)
print()

# число в двоичной системе счисления
bin1 = 0b11101101
print(bin1)
print()

# число в восьмеричной системе счисления
oct1 = 0o765
print(oct1)
print()

# построение целого числа из другого значения
string = "15"
number = int(string)
print(number)
print(number + 5)
# string + 5 -- ошибка

#####################################

# истинное значение
bool1 = True

# ложное значение
bool2 = True

print(bool1)
print(bool2)

#####################################
# примеры вещественных чисел
a = 0.5
b = 3.2

# примеры вещественных чисел в экспоненциальной записи
c = 3.2e5  # 3.2 * 10**5
d = 1e-3   # 1 * 10**(-3)

print(a, b, c, d)

# построение вещественного значения
print(float("0.5"))  # из строки
print(float(3))      # из целого числа

#####################################
# примеры комплексных чисел
c1 = 2 + 3j  # 2 + 3i, 2 - действительная часть, 3 - мнимая
c2 = 5 - 5j  # 5 + 5i

# построение комплексного числа из вещественных
a = 2
b = 3
c3 = complex(a, b)
c4 = complex(5, -5)

print(c1, c2)
print(c3, c4)


# переменные - имена, которые привязываются к объектам
var = 'I am a string'
print(var)
print(type(var))  # type(var) возвращает тип объекта, на который ссылается var

print()

# их можно привязывать к новым значениям
var = 42
print(var)
print(type(var))

print()

# однако нужно понимать, какой тип в данный момент может
# иметь объект и смешивать несовместимые типы нельзя
a = 5
b = 5
print(a + b)  # два числа сложить можно

b = '5'
print(a + b)  # число со строкой - нет (получаем ошибку)

#####################################
x = 2
y = 8
print(x + y)  # сложение
print(x + 3)
print(x - y)  # вычитание
print(x * y)  # произведение
print(x / y)  # деление
print(x // y) # целочисленное деление
print(x % y)  # остаток от деления
print(x ** y) # возведение в степень
print(3.2 * 0.8 - 2 * 5 - 3**3)  # арифметическое выражение
print(4 ** 0.5)  # возведение в степень 0.5 – квадратный корень

z = -2
print(abs(z))             # модуль числа
print(pow(z, 2), z ** 2)  # квадрат числа

m = 3.26
print(round(m), round(m, 1))  # округление числа до целого и до одного знака после запятой

#####################################
import math  # импротируем модуль math

x = 3.265
# целое число, ближайшее целое снизу, ближайшее целое сверху
print(math.trunc(x), math.floor(x), math.ceil(x))

print(math.pi)  # константа пи
print(math.e)   # число Эйлера

y = math.sin(math.pi / 4)  # math.sin – синус
print(round(y, 2))

y = 1 / math.sqrt(2)  # math.sqrt – квадратный корень
print(round(y, 2))


#####################################
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


#####################################
a = 2
b = 5

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


#####################################
# примеры строк
s1 = "Строка 1"
s2 = 'Строка 2'
print(s1, s2)

# конструирование строки из другого значения
s3 = str(8)
print(s3)

# многострочные строки
s4 = """Lesson2. Variables and Data Types
Some data types explained in this lesson:
 - int
 - bool
 - float
 - complex
 - str
"""
print(s4)

# \ используется, чтобы продолжить строку
# или любое выражение в Python со следующей строчки кода
s5 = "started\
      continued"
print(s5)



#####################################
str1 = 'hel'
str2 = 'lo'
result = str1 + str2  # конкатенация строка
print(result)


# форматирование строк

a = 48
b = 73

message1 = '%d + %d = %d' % (a, b, a + b)
print(message1)

message2 = '{} - {} = {}'.format(a, b, a - b)
print(message2)


# индексация строк

s = 'Hello, World!'

# (вернуться в седьмом уроке)
print(s[0])   # индексация начинается с нуля
print(s[4])   # четвёртый (пятый логически) элемент (символ)
print(s[-1])  # отрицательные числа – индексация с конца

print(s[2:7])    # символы со второго (включительно) по пятый (не включительно)
print(s[2:7:2])  # то же, но с шагом два


#####################################
# указываем разделитель
print(2, 3, 5, sep='; ')
print('he', 'llo', sep='')  # он может быть и пустой строкой

# указываем конец строки
print(1, end=' ')
print(2, end='\n\n')  # два перевода строки
print('he', end='')    # пустой конец
print('llo')


#####################################
# Ввод строки
string = input('Введите строку: ')
print('Вы ввели "', string, '"', sep='')

# Приглашение можно не указывать:
#         string = input()
# Результат, который возвращает любая функция,
# можно не привязывать ни к какому имени.
# Таким образом, следующая строка просто заставит
# программу ждать, пока пользователь что-то
# введёт или просто нажмёт Enter, а затем
# она продолжит выполнение.
input()


# введём два числа
n = int(input('Введите первое число: '))
m = int(input('Введите второе число: '))
print('{} + {} = {}'.format(n, m, n + m))
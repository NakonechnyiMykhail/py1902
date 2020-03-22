"""
#1
f1 = open('text.txt', 'r')
#2
f2 = open('~/py1902/start/lesson26/text.txt', 'r')
#3
f3 = open('data/text.txt', 'r')
#4
f4 = open('data/text.txt', mode='r', encoding='utf-8')
f4 = open('data/text.txt', mode='r', encoding='cp1252') #windows

r = открытие на чтение (по умолчанию)
w = открытие на запись
x = открытие на запись
a = дописывать информацию в конец файла
b = открытие в двоичном режиме
t = открытие в текстовом режиме (по умолчанию)
+ = открытие на чтение и на запись

rb = чтение в 2 режиме
"""
# write
# file = open('data1.txt', 'w')

# for index in range(10,20):
#     file.write(str(index) + '\n')

file = open('data2.txt', 'w')
for index in range(5):
    file.write(str(input('Enter line ' + str(index+1) + ': ')) + '\n')


file.close()


# read

file2 = open('data2.txt')
# print(file2.read())
# print(file2.read(1))

for line in file2:
    print(line)


file2.close()
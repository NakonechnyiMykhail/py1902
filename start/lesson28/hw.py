import os
from random import randint

def get_name():
    name = str(input('Enter the name of file: '))
    return name


def get_random_number(startNumber, endNumber):
    # random function
    return randint(startNumber, endNumber)

def write_random(file, count_of_number, startNumber, endNumber):
    for index in range(count_of_number):
        file.write(str(get_random_number(startNumber, endNumber)) + '\n')


def main():
    folder_name = 'file'
    # file_name = get_name()

    try:
        os.mkdir(folder_name)
    except FileExistsError:
        print('Folder has already created.')
    except Exception:
        print('Error???')
    # else:
    #     print('OK')
    finally:
        print('end folder create.')

    path = '/home/ubuntu/py1902/start/lesson28/' + folder_name + '/' + get_name() +'.txt'

    count = int(input('Enter count of numbers: '))
    start_number = int(input('Enter first number: '))
    end_number = int(input('Enter end number: '))

    try:
        file = open(path, mode='w+', encoding='utf-8')
        write_random(file, count, start_number, end_number)
    except UnboundLocalError:
        print('local variable "file" referenced before assignment')
    except FileNotFoundError:
        print('No such file or directory: '+ path)
    except TypeError:
        print('type error')
    except Exception:
        print('Error???')
    # else:
    #     print('OK')
    finally:
        file.close()
        print('File is closed.')







    # os.mkdir(folder_name)
    # file_name = get_name()


    # with open(path+folder_name +'/'+file_name+'.txt', encoding='utf-8') as file:
    # with open('test.txt', encoding='utf-8') as file:
    #     print(file.read())








if __name__ == '__main__':
    main()
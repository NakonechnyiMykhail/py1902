from func import *

def main():
    numbers = []
    for index in range(0,10):
        numbers.append(getRandomNumber())
        print(numbers[index])

    # print('index 3 = ', numbers[3])

    print('Avarage  = ', avarage(numbers))
    print('Summa    = ', summa(numbers))
    print('Summa2   = ', summa2(numbers))



if __name__ == '__main__':
    main()
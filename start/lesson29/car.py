class Car:

    # name = 'x5'
    # make = 'bmw'
    # model = 2010
    motor = 3.0
    color = 'black'

    count = 0
    #seets = 5
    #wheels = 4

    def start(self, name, make, model):
        message = 'Start motor'
        print(message)
        self.name = name
        self.make = make
        self.model = model
        # Car.count += 1

        # print('Start motor (car ', Car.count, ')')

        # return message

    def start2(self, a, b=None):
        if b is not None:
            print(a+b)
        else:
            print(a)

    def stop(self):
        print('Stop motor')

    def print_details(self):
        print('This is a Car class')

    @staticmethod
    def get_class_details():
        print('This is a Car class')

    def __str__(self):
        return 'Car class object'

    def __init__(self):
        Car.count += 1
        print(Car.count)
        self.name = 'corolla'
        self.__make = 'toyota'
        self._model = 2005


class SportCar(Car):
    def sportcar_method(self):
        print('this is 2 class')

    def print_details(self):
        print('This is a SportCar class')


class BigCar(Car):
    def big_method(self):
        print('this is 3 class')

# public
# private
# protected

car_1 = Car()
# car_1.start('a3','audi',2012)
# print(car_1.count)
# print(car_1.message)
# print(car_1.name)
# print(car_1.make)
# print(car_1.model)

car_2 = Car()
# car_2.start('a7','audi',2015)
# print(car_2.count)

# Car.get_class_details()
# print(car_1)

##########################################################################
# полиморфизм
car_1.start2(10)
car_1.start2(10, 20)


##########################################################################
# наследование
s_car_1 = SportCar()
# s_car_1.sportcar_method()
# print(s_car_1.name)

# s_car_1.start()


car_1.print_details()
s_car_1.print_details()
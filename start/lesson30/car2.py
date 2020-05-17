class Car:

    def __init__(self, model):
        self.model = model


    @property
    def model(self):
        return self.__model

    # set -> setter  | get -> getter
    @model.setter
    def model(self, model):
        if model < 2000:
            self.__model = 2000
        elif model > 2020:
            self.__model = 2020
        else:
            self.__model = model

    def getCarModel(self):
        return 'Year of model: ' + str(self.model)



# public    |
# private   | __name
# protected | _name

##########################################################################
# инкапсуляция

car_1 = Car(1987)

print(car_1.getCarModel())

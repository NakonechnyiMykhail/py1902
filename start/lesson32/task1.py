"""
1.
создать класс               : MyBox
создать внутри переменную   : number = 10

создать конструктор класса
 - внутри инициализировать стандартные переменные   : weight/height/length = 10
создать внутри функции      :
                                getData -> print("weight = {0} / height = {1} / length = {2}".format(w,h,l))
                                getVolume -> print("Volume of my box = ", h*l*w)
___________________________________________

2. создать экземпляр класса
3. получить данные
4. вывести объем
"""
class MyBox:

    def __init__(self, weight = 10, height = 10, length = 10):
        self.weight = weight
        self.height = height
        self.length = length

    def getData(self):
        print("weight = {0} / height = {1} / length = {2}".format(self.weight,self.height,self.length))

    def getVolume(self):
        print("Volume of my box = ", self.height*self.length*self.weight)


box = MyBox()
box.getData()
box.getVolume()

box2 = MyBox(5, 5, 5)
box2.getData()
box2.getVolume()

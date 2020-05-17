# parent class
class Bird:

    def __init__(self):
        print('Bird is ready')

    def whoIsThis(self):
        print('Bird')

    def sing(self):
        print('Bird sings')

# child class
class Parrot(Bird):

    def __init__(self):
        super().__init__() # => Bird is ready
        print('Parrot is ready')

    def whoIsThis(self):
        print('Parrot')


    def dance(self):
        print('Parrot is now dancing')


par = Parrot()
par.whoIsThis()
par.sing()
par.dance()
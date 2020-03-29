class Parrot:
    species = 'bird'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return '{} sings {}'.format(self.name, song)

    def dance(self):
        return '{} is now dancing'.format(self.name)


# class Example:
#     pass

x = int(2)
obj1 = Parrot('Blu', 10)
obj2 = Parrot('Woo', 15)

print(obj1.name)
print(obj1.age)
print(obj1.species)

print(obj1.sing("'Happy'"))
print(obj1.dance())
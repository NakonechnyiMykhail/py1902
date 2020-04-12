class MyClass:
    pass

class A:
    pass

class B:
    pass

class Person:
    name = 'Ivan'
    age = 10
    address = 'Kharkov'
    phone_number = '+380677777777'

    def set(self, name, age):
        self.name = name
        self.age = age

vlad = Person()
print(vlad.name)

vlad.set('Vlad', 15)
print(vlad.name)
def outer_function():
    var = 8  # создание локальной переменной var

    def inner_function():
        # указывает, что необходимо использовать переменную из внешней функции
        nonlocal var
        print(var)  # 8
        var = 10

    print(var)  # 8
    inner_function()  # вызов внутренней функции
    print(var)  # 10


# создание глобальной переменной var
var = 0
print(var)  # 0
outer_function()
print(var)  # 0
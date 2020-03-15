def outer_function():
    # объявление функции локально
    def inner_function():
        print('Внутренняя функция')
    print('Внешняя функция')
    # вызов функции
    inner_function()

# вызов внешней функции
outer_function()

# inner_function()  # ошибка, здесь эта функция недоступна
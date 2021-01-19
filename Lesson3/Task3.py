def my_func(arg1, arg2, arg3):

    try:
        if int(arg1) and int(arg2) and int(arg3):                       # проверяем на соответствие числу и перехватываем символьный ввод
            return sum([arg1, arg2, arg3]) - min([arg1, arg2, arg3])    # удаляем минимальный аргумент
        else:
            return "ошибка аргументов"
    except ValueError as error:
        print(f"Введено не цифровое значение {error}")


print(f"Искомый аргумент {my_func(14, 2, 5)}")

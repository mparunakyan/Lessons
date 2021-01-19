def checksum(symbol_string):
    # Функция проверки содержания не английского символа в малом регистре
    # При первом же символе не соответствующем условия, система возвращает False,
    # что исключает элемент списка из выборки
    # Раскомментируйте соответствующие строки, чтобы проверить сами символы
    # Код приведен под стандарт PEP 8
    for i in list(symbol_string):
        # print(ord(i))
        if ord(i) < 97 or ord(i) > 122:
            # print(f"Найден символ {i}")
            return False
    return True


origin_string = "nice авп ъghj jапро hjjпаро вапрghgh cool"
astr = origin_string.split()  # Получение из строки списка
newstr = list(filter(checksum, astr))  # Преобразование в список отфильтрованного списка
print(" ".join(newstr).title())  # Вывод предложения

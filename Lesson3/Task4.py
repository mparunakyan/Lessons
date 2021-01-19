def my_func(x, y):
    i = 0
    numcalc = x
    while i < abs(round(y)):  # Производим умножение x на само себя y раз
        numcalc *= x
        i += 1
    return round(1 / numcalc, 5)  # преобразуем отрицательную степень в вид 1/х, округляем до 5 символа после запятой


print(my_func(4, -4.5))  # Пример применения

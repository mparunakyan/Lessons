revenue = int(input("Введите выручку: "))
expenses = int(input("Введите расходы: "))

if expenses==0 or (type(expenses)==str):
    print("Введено значение 0 либо тектовая строка, производим коррекцию на 1")
    expenses = 1

if revenue > expenses :
    print("Доходный период")
    print("Рентабельность - " + str(((revenue - expenses) // revenue)*100) + "%")
    persnum = int(input("Введите количество персонала: "))
    if persnum == 0 or (type(persnum) == str):
        print("Введено значение 0 либо тектовая строка, производим коррекцию на 1")
        persnum = 1
    print("Прибыль компании в расчете на одного сотрудника - " + str((revenue - expenses) // persnum) + "руб.")

elif revenue<expenses:
    print("Убыточный период")
elif revenue < expenses :
    print("Безубыточный период")


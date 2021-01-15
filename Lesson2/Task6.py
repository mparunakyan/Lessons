#base = [ (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
#         (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
#         (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
#         ]
base = []       # пустая база товаров
names = []      # список имен товаров
prices = []     # список цен товаров
pcs = []        # список количества товаров
meaunit = []    # список единиц измерений
analit = dict() # аналитический словарь
ind = 1         # индекс заводимых товаров в базу
while True:
    if input("Добавляем новый товар? (y/n): ").lower() == "y": # запрос на добавление
        item = input("Введите название товара, цену, количество, единицу измерения: ") # ввод товара одной строкой
        item=list(item.split(","))  # представление в виде списка
        product = ({"название" : item[0], "цена":item[1], "количество":item[2], "eд":item[3]}) # формирование словаря товара
        base.append((ind,product)) # добавление товарной строки с индексом в базу
        ind +=1
    else:
        print(' \n' * 25) # очистка экрана
        break
for i in base:
    names.append(i[1].get("название")) # формирование списка имен
    prices.append(int(i[1].get("цена"))) # формирование списка цен
    pcs.append(int(i[1].get("количество"))) # формирование списка количества
    if i[1].get("eд") not in meaunit:
        meaunit.append(i[1].get("eд")) # формирование списка уникальных единиц измерений
analit.update({"название" : names, "цена":prices, "количество":pcs, "eд":meaunit}) # формирование аналитики
print(f"{'_'*5} Аналитика {'_'*5}")
print(analit) # вывод аналитики
# я спать, за полночь...
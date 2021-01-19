def dataprint(**kparams):
    """
    Принимаем на входе именованные параметры в любом количестве и в виде словаря
    Также можно в виде списка и кортежей, но словарем удобнее будет выводить в произвольном порядке )))
    """
    return kparams

pers_data = dataprint(name="Гарик", surname="Кузнецов", year="1969", city="Москва", email="email@email.com", phone="+7 495 777 77 77")
print(f"Имя {pers_data.get('name')}, Фамилия {pers_data.get('surname')}, Год {pers_data.get('year')}, Город {pers_data.get('city')}, Почта {pers_data.get('email')}, Телефон {pers_data.get('phone')}, ")
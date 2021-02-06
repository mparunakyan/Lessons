class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def get_date(cls, date):
        day = str(date.split("-")[0])
        month = str(date.split("-")[1])
        year = str(date.split("-")[2])
        Data.check_date(cls(day, month, year))
        return cls(day, month, year)

    @staticmethod
    def check_date(obj):
        if int(obj.year) > 2050 or int(obj.year) <= 0:
            print(f"There is a mistakes in year {obj.year}")
        else:
            print(f"No mistakes in value of the year {obj.year}")
        if int(obj.month) > 12 or int(obj.month) <= 0:
            print(f"There is a mistakes in month {obj.month}")
        else:
            print(f"No mistakes in value of the month {obj.month}")
        if int(obj.month) in [1, 3, 5, 7, 8, 10, 12] and (31 >= int(obj.day) > 0):  # Months with 31 days
            print(f"No mistakes in a day {obj.day} of month {obj.month}")
        elif int(obj.month) in [4, 6, 9, 11] and (30 >= int(obj.day) > 0):  # Months with 30 days
            print(f"No mistakes in a day {obj.day} of month {obj.month}")
        elif int(obj.month) == 2 and ((29 if int(obj.year) % 4 == 0 else 28) >= int(obj.day) > 0):  # Leap year 29 days
            print(f"No mistakes in a day {obj.day} of month {obj.month}")
        else:
            print(f"No such day {obj.day} of month {obj.month} of {obj.year} year")


my_date = "29-02-2021"
try:
    a = Data.get_date(my_date)
except ValueError as error:
    print(f"There is a symbols instead of integer: {error}")

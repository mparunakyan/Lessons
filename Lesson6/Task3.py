class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income.update({"wage":wage})
        self._income.update({"bonus": bonus})

class Position(Worker):
    def get_full_name(self):
        print(f"{self.name} {self.surname} {self.position}")

    def get_total_income(self):
        print(f"Total income is {self._income.get('wage') + self._income.get('bonus')}")


a = Position("Valentin", "Shappo", "CEO", 50, 50)
a.get_full_name()
a.get_total_income()
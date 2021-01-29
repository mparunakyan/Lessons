class Stationery:
    title = ""

    def __init__(self, name):
        self.title = name

    def draw(self):
        print(f"Start draw!")


class Pen(Stationery):
    def draw(self):
        print(f"We draw with {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"We draw with {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"We draw with {self.title}")


p = Pen("Pen")
p.draw()

print(5 * "*")

a = Pencil("Pencil")
a.draw()
print(5 * "*")

h = Handle("Handle")
h.draw()

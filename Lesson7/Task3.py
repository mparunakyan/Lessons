class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f"{self.cell}"

    def __add__(self, other):
        total_cells = self.cell + other.cell
        return Cell(total_cells)

    def __sub__(self, other):
        total_cells = self.cell - other.cell
        if total_cells > 0:
            return Cell(total_cells)
        else:
            print(f"Total number of cell less that 0")
            return None

    def __mul__(self, other):
        total_cells = self.cell * (
            other.cell if other.cell > 0 else 1)  # If the value of cell less or equal 0, reduce to 1
        return Cell(total_cells)

    def __truediv__(self, other):
        total_cells = self.cell // (
            other.cell if other.cell > 1 else 1)  # If the value of cell less or equal 0, reduce to 1
        return Cell(total_cells)

    def make_order(self, symbol_number):
        if symbol_number <= 0:
            print("Wrong length")
        else:
            for _ in range(self.cell//symbol_number):
                print('@' * symbol_number)
            print('@' * (self.cell % symbol_number) if (self.cell % symbol_number) > 0 else "")

cell_1 = Cell(15)
cell_2 = Cell(15)
cell_3 = Cell(20)
cell_4 = cell_3 + cell_2  # We can create new cell from two previous cells and use it

print(f"Sum of cells {cell_1 + cell_2 + cell_3}")
print(f"Sub of cells {'is undefined' if (cell_1 + cell_2 - cell_3) is None else cell_1 + cell_2 - cell_3}")
print(f"Multiplication of cells {cell_1 * cell_2}")
print(f"Diving of cells {cell_3 / cell_1}")
cell_4.make_order(6)

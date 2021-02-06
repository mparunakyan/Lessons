class ComplexDigit:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        # print(self.real + other.real)
        # print(self.imaginary + self.imaginary)
        return f"{self.real + other.real} + {(self.imaginary + self.imaginary)}j"

    def __mul__(self, other):
        return f"{self.real * other.real - self.imaginary * other.imaginary} " \
                f" + {self.real * other.imaginary + other.real * self.imaginary}j"


a1 = int(input("Enter 'a' real part: "))
a2 = int(input("Enter 'a' imaginary part: "))
a = ComplexDigit(a1, a2)

b1 = int(input("Enter 'b' real part: "))
b2 = int(input("Enter 'b' imaginary part: "))
b = ComplexDigit(b1, b2)

print(f"a + b = {a + b}")
print(f"a * b = {a * b}")

class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, operand):
        return Complex(self.a + operand.a, self.b + operand.b)

    def __sub__(self, operand):
        return Complex(self.a - operand.a, self.b - operand.b)

    def __mul__(self, operand):
        return Complex(
            self.a * operand.a - self.b * operand.b,
            self.a * operand.b + self.b * operand.a,
        )

    def __neg__(self):
        return Complex(-self.a, -self.b)

    def __str__(self):
        if self.b < 0:
            return f'{self.a} - {abs(self.b)}i'
        else:
            return f"{self.a} + {self.b}i"
    
A = Complex(1,2)
B = Complex(3,4)

print(A + B)
print(A - B)
print(A * B)
print(-A)

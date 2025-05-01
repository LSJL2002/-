class Complexnumbers:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    
    def __add__(self,operand):
        return Complexnumbers (self.a + operand.a, self.b + operand.b)
    
    def __subtract__(self, operand):
        return Complexnumbers (self.a - operand.a, self.b - operand.b)
    
    def __multiplication__(self, operand):
        real =
        img = 
        return Complexnumbers()
    
    def __str__(self):
        return f"{self.a} + {self.b}i"
    
A = Complexnumbers(1,2)
B = Complexnumbers(3,4)

print(A + B)
print(A - B)
print(A * B)
print(-A)
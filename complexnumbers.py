class Complexnumbers:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    
    def __add__(self,operand):
        return Complexnumbers (self.a + operand.a, self.b + operand.b)
    
    def __subtract__(self, operand):
        return Complexnumbers (self.a - operand.a, self.b - operand.b)
    
    def __multiplication__(self, operand):
        return Complexnumbers ()
    
    def __str__(self):
        return f"{self.a} + {self.b}i"
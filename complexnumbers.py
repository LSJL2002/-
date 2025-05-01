class Complexnumbers:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    
    def __add__(self,operand):
        return Complexnumbers (self.a + operand.a, self.b + operand.b)
    


A = Complexnumbers(1,2)
B = Complexnumbers(3,4)

C = A + B
print(C)

    '''
    def subtraction(self,a,b):

    
    def inverse(self,a,b):

    def multiplication(self,a,b):
    '''
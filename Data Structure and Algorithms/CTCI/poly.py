class Polynomial:
    def __init__(self, *args):
        
        self.coef = args

    def __repr__(self):
        """ Dunder method of representation"""
        return " {}x^2 + {}x + {} ".format(*self.coef) 
    
    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.coef, other.coef)))


p1 = Polynomial(1,2,3)
p2 = Polynomial(2,4,-7)

 
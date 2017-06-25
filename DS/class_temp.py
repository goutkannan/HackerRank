# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 16:11:48 2017

@author: Goutham
"""

class A:
    a = 1
    b = 2.0
    _C = 12
    def __init__(self,a):
        
        self._a =" protected"
        self.__a = "private"
        
    def modnprint(self,a):
        self.a = a
        print(a)
        
    def __repr__(self):
        return "place holder"
    
class B(A):
    def __init__(self):
        print(A._a)

       



obj1 = A(1)
print(obj1._C)  
obj1._C =5 


print(obj1._C) 

print(A._C) 

obj2 = A(1) 
print(obj2._C)


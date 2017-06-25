# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Stack:
    
    def __init__(self):
        self.stack=[]
    def isEmpty(self):
        return len(self.stack) == 0
        
    def push(self,data):
        self.stack.append(data)
        return True
    
        
    def pop(self):
        if not self.isEmpty():
           return self.stack.pop()
        else:
            return None 
            
            
    def peek(self):
        return self.stack[len(self.stack)-1]
  
        
        
        
st = Stack()
st.push("hi")
st.push(2.2)
st.push(3)
print(st.isEmpty())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.isEmpty())
print(st.pop())
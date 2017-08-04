"""
Problem

Your friend John uses a lot of emoticons when you talk to him on Messenger. In addition to being a person who likes to express himself through emoticons, he hates unbalanced parenthesis so much that it makes him go :(

Sometimes he puts emoticons within parentheses, and you find it hard to tell if a parenthesis really is a parenthesis or part of an emoticon.

A message has balanced parentheses if it consists of one of the following:

An empty string ""
One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a colon)
An open parenthesis '(', followed by a message with balanced parentheses, followed by a close parenthesis ')'.
A message with balanced parentheses followed by another message with balanced parentheses.
A smiley face ":)" or a frowny face ":("
Write a program that determines if there is a way to interpret his message while leaving the parentheses balanced.
"""

smiley =':)'
frowny=':('

def chk(string):
    s=[]
    count=0
    colonflag= False
    for c in string:
        
               
        if c=='(':
            if colonflag:
                s.append(':(')
                colonflag = False 
            else:
                s.append('(')
        elif c==')':
            if '(' in s: 
                s.pop(s.index('('))
            elif ':(' in s:
                s.pop(s.index(':('))
            elif colonflag:
                s.append(":)")
                
            else:
                s.append(')')
            colonflag = False
        else:
            colonflag = False
        
        if  c==':':
            if ':' in s[-1:]:
                s.pop()
            colonflag = True


    for x in s:
        if x !=smiley and x!=frowny:
            count+=1
    
    
    return "YES" if count==0 else "NO" 

def check_balance(src):
    opt_open = opt_close = 0
    count = 0
    has_eyes = False

    for char in src:
        if char == '(':
            if has_eyes:
                opt_open += 1
            else:
                count += 1

        elif char == ')':
            if has_eyes:
                opt_close += 1
            elif count > 0:
                count -= 1
            # if needed pair with an optional parens
            elif opt_open > 0:
                opt_open -= 1
            else: 
                return False

        if opt_close > count:
            opt_close = count

        has_eyes = (char == ':')
    return count <= opt_close

print("FALSE"== check_balance("()())()"))
print("YES"== check_balance("start :):)"))
print("YES"== check_balance("(:)"))
print("NO"== check_balance(":))"))
print("YES"== check_balance(":(:):)"))

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

from collections import Counter


import sys

def isValid(s):
    flag=0
    c= Counter(s)
    print(c)
    l = c.values()
    print(c.most_common(1))
    maxCount = int(c.most_common(1)[0][1]) 
    sum=0
    l = [ maxCount-x for x in l]
    print(l) 
    for x in l:
         sum +=abs(x)
     

    if sum>1:
       return "NO"
    else:
       return "YES"

         # Complete this function

s = input().strip()
result = isValid(s)
print(result)

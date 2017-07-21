import sys
import re

n = int(input().strip())
s = input().strip()
k = int(input().strip())
if(k>26):
    k = k%26
for ch in s:
    flag =0
    if(ch.isupper()):
        ch = ch.lower()
        flag=1

    cValue = ord(ch) + k 
    zValue = ord('z')
    if re.match("[a-zA-Z]",ch):
        if cValue > zValue:
            c = chr(ord('a') + cValue-zValue-1)
            if flag==1:
                print(c.upper(),end="")
            else:
                print(c,end="")
        else:
            if flag==1:
                print(chr(ord(ch)+k).upper(),end="")
            else:
                print(chr(ord(ch)+k), end="")
    else:
        print(ch, end="")


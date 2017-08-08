import sys
import math
s="haveaniceday"
s = s.replace(" ","")

n = len(s)

floor = math.floor(math.sqrt(n))
ceil = math.ceil(math.sqrt(n))

row = floor
column = ceil 

while(row*column < n):
  if(floor<=row<=column<=ceil):
    row+=1
    
strlen=0
for i in range(0,row+1):
    if(strlen<n):
      print(s[i::column],end=" ")
      strlen+=len(s[i::column]) 
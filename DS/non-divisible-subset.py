from collections import Counter
import math
"""
Main idea:  
1. Store the remainders of all the input integers
2. For all entries that are divisible by k(i.e) rem = 0 , add 1 to the counter
3. For all remainders  i from 1 to k/2+1, add the max count between i,k-i , except when i=k-i for this case
increment the counter by 1 
"""

n,k = input().strip().split(' ')
n,k = [int(n),int(k)] 
numbers = [int(x) for x in  input().split()]

remainders = [0]*k 
for i in numbers:
    remainders[i%k] +=1 
#print(remainders)
count = 1 if (remainders[0]>0 ) else 0
for i in range(1, int(k/2)+1):
    if i != k-i:
        count+= max(remainders[i],remainders[k-i])
    else:
        count+=1

print(count)

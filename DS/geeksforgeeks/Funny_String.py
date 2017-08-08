"""
Suppose you have a String, , of length  that is indexed from  to . You also have some String, , that is the reverse of String .  is funny if the condition  is true for every character  from  to .

Note: For some String ,  denotes the ASCII value of the  -indexed character in . The absolute value of an integer, , is written as .

Input Format

The first line contains an integer,  (the number of test cases). 
Each line  of the  subsequent lines contain a string, .

Constraints

Output Format

For each String  (where ), print whether it is  or  on a new line.

Sample Input

2
acxz
bcxz
Sample Output

Funny
Not Funny


Explanation

Test Case 0:  
 
 
 
As each comparison is equal, we print .

Test Case 1:  
, but  
At this point, we stop evaluating  (as ) and print .
"""


import sys

def funnyString(s):
    # Complete this function
    rs = s[::-1]
    for i in range(1,len(s)):
      if abs(ord(rs[i-1])-ord(rs[i]))!=abs(ord(s[i-1])-ord(s[i])):
        return "Not Funny"
    return "Funny"
  
      

q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = funnyString(s)
    print(result)
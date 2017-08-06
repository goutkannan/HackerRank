"""

A top secret message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent. You have to determine the total number of ways that message can be decoded.
Note: An empty digit sequence is considered to have one decoding. It may be assumed that the input contains valid digits from 0 to 9 and If there are leading 0’s, extra trailing 0’s and two or more consecutive 0’s then it is an invalid string.

Example :
Given encoded message "123",  it could be decoded as "ABC" (1 2 3) or "LC" (12 3) or "AW"(1 23).
So total ways are 3.

Input:
First line contains the test cases T.  1<=T<=1000
Each test case have two lines
First is length of string N.  1<=N<=40
Second line is string S of digits from '0' to '9' of N length.

Example:
Input:
2
3
123
4
2563
Output:
3
2
 
"""
def countMsg(numbers,n):
    count =[1,1]
    for i in range(2,n+1):
        count.append(0)
        if numbers[i-1]>0:
            count[i]=count[i-1]
        
        if (numbers[i-2] ==1 or( numbers[i-2]==2 and numbers[i-1] <7 )):
            count[i]+=count[i-2]

    return count[-1]



#n = int(input())
#strlist = input() 

n=3
strlist = "122"


assert "00" not  in strlist,"Invalid string"
assert "0" not in strlist[::-2],"0"

if(len(strlist.strip())==0):
    print("1")
else:
    strlist = [int(x) for x in strlist ]
    print(countMsg(strlist,n))






















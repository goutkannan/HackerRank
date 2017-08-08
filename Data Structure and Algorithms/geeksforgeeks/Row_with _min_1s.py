"""
Determine the row index with minimum number of ones. The given 2D matrix has only zeroes and ones and also the matrix is sorted row wise . If two or more rows have same number of 1's than print the row with smallest index.
Note: If there is no '1' in any of the row than print '-1'.
Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case consists of two integer n and m. The next line consists of n*m spaced integers. 
Output:
Print the index of the row with minimum number of 1's.
Constraints: 
1<=T<=100
1<=n,m<=100

Example:
Input:
2
3 3
0 0 0 0 0 0 0 0 0
4 4
0 0 0 1 0 1 1 1 0 0 1 1 0 0 1 1

Output:
-1
0
"""

def getRow(n,m,intlist):
    min_count = n*m 
    min_idx = -1 
    notZero = False 

    for i in range(n):
        count=0
        for j in range(m):
            if(intlist[(m*i)+j] ==1):
                count +=1
                notZero = True
        if count<min_count:
            min_count =count 
            min_idx = i

    if notZero:
        return min_idx
    else:
        return-1





#n,m =  input().strip()
#n,m  = [int(n),int(m)]
#text = input() 

n,m = [4,4]
text = "0 0 0 1 0 1 1 1 0 0 1 1 0 0 1 1"

number =[int(x) for x in text.split()]

print(getRow(n,m,number))
 
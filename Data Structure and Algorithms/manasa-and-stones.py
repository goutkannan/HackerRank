"""
Manasa is out on a hike with friends. She finds a trail of stones with numbers on them. She starts following the trail and notices that two consecutive stones have a difference of either  or . Legend has it that there is a treasure trove at the end of the trail and if Manasa can guess the value of the last stone, the treasure would be hers. Given that the number on the first stone was , find all the possible values for the number on the last stone.

Note: The numbers on the stones are in increasing order.

Input Format

The first line contains an integer , i.e. the number of test cases.  test cases follow; each has 3 lines. The first line contains  (the number of stones). The second line contains , and the third line contains .

Constraints

Output Format

Space-separated list of numbers which are the possible values of the last stone in increasing order.

Sample Input

2
3 
1
2
4
10
100
Sample Output

2 3 4 
30 120 210 300 
Explanation

All possible series for the first test case are given below:

0,1,2
0,1,3
0,2,3
0,2,4
Hence the answer 2 3 4.

Series with different number of final steps for second test case are the following:

0, 10, 20, 30
0, 10, 20, 120
0, 10, 110, 120
0, 10, 110, 210
0, 100, 110, 120
0, 100, 110, 210
0, 100, 200, 210
0, 100, 200, 300
Hence the answer 30 120 210 300
"""

def Manasa():
    """
    Implementation based on the logic that addition is commutative (i.e) a + b + a = a + a + b and b + b + a = a + b + b 
    Hence for a given N the possible sums of a,b is sorted set of
    (n-1)a + 0b
    (n-2)a + 1b
    (n-3)a + 2b
    ....
    .... 
    END = Nth time. 
    """

    T = int(input())
    while T:
        result_set = set()
        n = int(input())
        a = int(input())
        b = int(input())
        for i in range(n):
            val = (n-i-1) * a + i * b
            result_set.add(val)
        # Print the sorted set
        for value in sorted(result_set):
            print(value, end=" ")
        print()
        T -= 1


if __name__ == '__main__':
    Manasa()

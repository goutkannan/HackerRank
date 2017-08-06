"""
Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y co-ordinates of two points: the left top corner and the right bottom corner of the rectangle.

Note that two rectangles sharing a side are considered overlapping.                      

Input:

The first integer T denotes the number of test cases. For every test case, there are 2 lines of input. The first line consists of 4 integers: denoting the co-ordinates of the 2 points of the first rectangle. The first integer denotes the x co-ordinate and the second integer denotes the y co-ordinate of the left topmost corner of the first rectangle. The next two integers are the x and y co-ordinates of right bottom corner. Similarly, the second line denotes the cordinates of the two points of the second rectangle.


Output:

For each test case, output (either 1 or 0) denoting whether the 2 rectangles are overlapping. 1 denotes the rectangles overlap whereas 0 denotes the rectangles do not overlap.


Constraints:

1 <= T <= 10

-10000 <= x,y <= 10000

T denotes the number of test cases. x denotes the x co-ordinate and y denotes the y co-ordinate.


Example:

Input:

2
0 10 10 0
5 5 15 0
0 2 1 1
-2 -3 0 2

Output:

1
0

Solution: 
Going for the reverse theory

number of non overlapping cases are easier to find than overlapping cases. 
So find out if the given trianlges are side by  to each other or stacked up and down. If the caes is neither of these two then 
the rectangels must overlap. 

"""
class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    



def chk_overlap(l1,r1,l2,r2):
    #make sure to assert args for point type
    if l2.x>r1.x or r2.x < l1.x:
        return 0
    if r1.y > l2.y or r2.y > l1.y:
        return 0

    return 1




#T = int(input())
T=1
input1 = "0 10 10 0"
input2 = "5 5 15 0"
while(T>0):
    p1 = [int(x) for x in input1.split()]
    x,y = p1[:2]
    l1 = point(x,y)
    x,y = p1[2:]
    r1 = point(x,y) 

    p2 = [int(x) for x in input2.split()]
    x,y = p2[:2]
    l2 = point(x,y)
    x,y = p2[2:]
    r2 = point(x,y)
    
    print(chk_overlap(l1,r1,l2,r2))
    T-=1

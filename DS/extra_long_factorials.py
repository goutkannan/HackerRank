from collections import deque
def multiply(n,digits):
    product=0
    val=0
    carry=0
    for i in range(len(digits),0,-1):
        product = n*digits[i-1]
        product+=carry
        
        val = product%10
        digits[i-1] = val

        carry = int(product/10)
    
    while(carry!=0):
        val = carry%10
        digits.appendleft(val)
        carry  = int(carry/10)
    
    return digits 





#number_str = "1234432123457900948694039"
number_str  = "2345"

str_list = [int(str) for str in  number_str]
number = deque(str_list) 



n = int(number_str)
while(n>1):
    n-=1
    number = multiply(n,number)


print(len(number))


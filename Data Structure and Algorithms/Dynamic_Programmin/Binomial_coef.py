def calcaulate_coef(n, k):
    if k == 0:
        return 1
    if n == 0:
        return 0
    if k > n:
        return -1
    value = 1
    for i in range(n, 0, -1):
        if i > n-k:
            value *= i
        if i <= k:
            value /= i
    
    return value

def  binomial_coeff(n,k):
    if k==0 or n==k:
        return 1
    return binomial_coeff(n-1, k-1) + binomial_coeff(n-1, k)

def main():
    print(calcaulate_coef(7,3)==35)
    print(calcaulate_coef(4,3)==4)
    print(calcaulate_coef(7,0)==1)
    print(calcaulate_coef(5,2)==10)
    print(calcaulate_coef(7,13)==-1)
    print(binomial_coeff(7, 3))


if __name__ == '__main__':
    main()
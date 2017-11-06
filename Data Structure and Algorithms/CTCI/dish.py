"""
Yeild - Using generator functions by utilizing yeild
"""

def isPrime(n):
    if n == 1:
        return False

    for i in range(2, int(n/2)):
        if n%i == 0:
            return False
    return True

def primes(number):
    for i in range(1, number+1):
        if isPrime(i):
            yield i

def prime_number_generator():
    """ Uses generators to list all n prime number """
    end_num = 100
    for prime_num in primes(end_num):
        print(">", prime_num)

def test_area():
    """
    Print number from 1 - n as a string
    """
    n=100

    s = "".join([str(i) for i in range(n)])
    print(type(s),"..",s)

if __name__ == '__main__':
    print(prime_number_generator.__doc__)
    test_area()


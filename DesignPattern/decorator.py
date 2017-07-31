import time

def timeit(func):
    def decorated(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = float(time.time() -start)
        print("Ran in seconds",end)

        return result
    return decorated

#typical decorator usage
@timeit
def factorial(num):
    fact =1
    for i in range(2,num+1):
        fact*=i
    return fact

print("Calculation factorial of 20")
print(factorial(90))

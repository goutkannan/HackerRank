def isEven(i):
    return True if  1%2 == 0 else False

def permutationRunner(data, k):
    print("...> {} k= {}".format(data, k))
    if k==1:
        print(data)
    else:
        for i in range(0,k):
            permutationRunner(data, k-1)
            if i < k-1:
                print(" i= {} .... k ={}".format(i, k))
                if isEven(i):
                    data[i], data[k-1] = data[k-1], data[i]
                else:
                    data[0], data[k-1] = data[k-1], data[0]

def getPermuation(data):
    try:
        permutationRunner(data, len(data))
    except e:
        print("found {}".format(e))


getPermuation([1,2,3])


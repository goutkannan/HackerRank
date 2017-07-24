array = [1,2,3,5,7,8,9,10] 

def lower(n,s):
    if array[n]==s or (array[n-1]<s and array[n+1]>s):
        return n
    elif array[n]>s:
        return lower(n-1,s)
    else:
        if len(array)>n:
            return lower(n+1,s)
        else:
            return n

def higher(n,s):
    return lower(n,s)-1


i = int(input())

print(higher(int(len(array)/2),i))

print(lower(int(len(array)/2),i))

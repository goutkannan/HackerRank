M= [(1,2,3),(3,1,1),(2,2,1)]
n=3

def colSum(n,M):
    listsum=[]
    for j in range(n):
        temp=0
        for i in M:
            print(i[j],end=" ")
            temp+=i[j]
        print(',')
        listsum.append(temp)
    return sorted(listsum)

def pyColSum(n,M):
    return sorted(map(sum,zip(*M)))


if (sorted(map(sum,M)) == pyColSum(n,M)):
    print("possible")
else:
    print("Impossible")


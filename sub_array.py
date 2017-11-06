from collections import Counter

arr = [1,2,3,1,1,2,1,3,2,2]
c = Counter(arr)
val = c.most_common()

print(val)

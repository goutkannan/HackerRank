import re
from collections import Counter
def is_valid(s):
    m = re.match("(\w)((?!\\1)\w)(\\1\\2)*(\\1)?$",s)
    return m



string = "beabeefeab"
c = Counter(string).most_common()[::-1]
print(c)
tmax=0

for i in range(len(c)):
    for j in range(i+1,len(c)):
        if(c[i][1]+c[j][1] > tmax):
            pattern = "[^"+c[i][0]+c[j][0]+"]"
            if is_valid(re.sub(pattern,"",string)):
                tmax = c[i][1]+c[j][1]


print(tmax)




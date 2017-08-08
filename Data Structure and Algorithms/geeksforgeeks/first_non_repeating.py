from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    def __repr__(self):
        return '%r(%s)' % (self.__class__.__name__ , OrderedDict(self))
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

oc = OrderedCounter('abracadabra')
print(oc)

test = "Geeks foreverGeeks"

def first_uniqueChr(test):
    _char_count = Counter(test.replace(" ",""))

    for k,v in _char_count.items():
        if v==1:
            return k  

def optimized_uniqueChr(string):
    _chr_dict =OrderedCounter(string.replace(" ",""))
    _test_dict = Counter(string.replace(" ",""))

    for k,v in _chr_dict.items():
        if v==1:
            return k


#print(optimized_uniqueChr(test))
print(first_uniqueChr(test))




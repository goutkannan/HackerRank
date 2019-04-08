from collections import Counter
_test_str = "abccddde"
_test_weights = [1, 3,12, 5, 9,10]
BASE = ord("a") -1


def isWuS(test_str =_test_str, test_weights = _test_weights):
    buf = ""
    weight = 0
    wus = {}
    for i,val in enumerate(test_str):
        if val in buf or buf is "":
            buf += val
            weight = weight + ord(val) - BASE
        else:
            buf = val
            weight = ord(val) - BASE

        wus[buf] = weight

    weights  = set(wus.values())
    print(wus)
    print(weights)
    for q in test_weights:
        yield q in weights

if __name__ == "__main__":
    for res in isWuS():
        print(res)








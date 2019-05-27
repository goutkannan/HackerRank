"""Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
def longest_substr(inputStr):
    indexDict = {}
    start = 0
    end = 0
    maxlen = 0

    for idx, s in enumerate(inputStr):
        if s in indexDict:
            old_idx = indexDict[s]
            if old_idx in range(start, finish):
                indexDict[s] = idx
                start, finish = old_idx+1, finish
            else:
                indexDict[s] = idx
                start, finish = start, idx
        else:
            indexDict[s] = idx
            start, finish = start, idx
        l  = idx - start + 1
        if l >= maxlen:
            maxlen = l

    return maxlen





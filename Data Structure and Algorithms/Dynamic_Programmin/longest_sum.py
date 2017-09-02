def longest_contiguous_sum(array):
    max_till_now = array[0]
    max_global = array[0]
    for i in array:
        max_till_now += i
        if max_till_now < 0:
            max_till_now = 0
        elif max_till_now > max_global:
            max_global = max_till_now
    
    return max_global 


def longest_increasing_subsequence(array):
    """ DP Solution to find the longest increasing subsequence """
    table = [1]*len(array)
    for i in range(1, len(array)):
        for j in range(0, i):
            if array[i] > array[j] and table[i] < table[j]+1:
                table[i] = table[j] + 1

    return max(table)


def main():
    inputList = [1, 20, 4, 30, 6, 40, 7, 45]
    print(longest_increasing_subsequence(inputList))

if __name__ == '__main__':
    main()
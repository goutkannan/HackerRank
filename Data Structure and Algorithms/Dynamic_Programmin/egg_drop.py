"""
DP Egg Drop problem , http://www.geeksforgeeks.org/dynamic-programming-set-11-egg-dropping-puzzle
"""
def eggdrop_dp(eggs, floors):
    """ Dynamic programming approach using memoization for each floor n egg
    """
    table = [[0 for i in range(floors + 1)] for j in range(eggs+1)]
    for i in range(0, floors + 1):
        # When the number of is one then the number of chances will be equal to the number of floors
        table[1][i] = i

    for row in table:
        print(row)

    for e in range(2, eggs+1):
        for f in range(1, floors+1):
            value = float('inf')
            for k in range(1, f+1):
                temp = max(table[e-1][k-1], table[e][f-k])
                if temp < value:
                    value = temp
            
            table[e][f] = temp

    print(table[eggs][floors])

def main():
    eggdrop_dp(2,6)

if __name__ == '__main__':
    main()
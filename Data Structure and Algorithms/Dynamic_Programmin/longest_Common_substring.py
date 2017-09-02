def lcs(m, n):
    if m==0 or n==0:
        return 0
    if S1[m-1] == S2[n-1]:
        return 1 + lcs(m-1, n-1)

    else:
        return max(lcs(m-1, n), lcs(m, n-1))


def lcs_dp(X, Y, m, n):
    table = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if X[i-1] == Y[j-1]:
                table[i][j] = 1 + table[i-1][j-1]
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1]) 
            
    return table[m][n]



S1 = "ABCDEFGH"
S2 = "AxByCzDZE"

print(lcs(len(S1), len(S2)) == lcs_dp(S1, S2, len(S1), len(S2)))



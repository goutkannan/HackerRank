inputMatrix = [[1, 1, 1, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1,0] ]

print(inputMatrix)
dp = [[0 for i in range(len(inputMatrix))] for j in range(len(inputMatrix))]

for row in range(1, len(inputMatrix)):
	for col in range(1, len(inputMatrix)):
		dp[row][col] = inputMatrix[row][col]


print(dp)
count =0 

for row in range(1, len(inputMatrix)):
	for col in range(1, len(inputMatrix)):
		if dp[row][col] ==1 and dp[row-1][col]==0 and dp[row][col-1]==0:
			count+=1






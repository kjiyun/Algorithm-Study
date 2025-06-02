import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip())))
dp = [[0]*m for _ in range(n)]
dp[0] = arr[0]

for i in range(n):
    dp[i][0] = arr[i][0]

for i in range(1, n):
    for j in range(1, m):
        if arr[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

max_len = 0
for k in range(n):
    tmp = max(dp[k])
    max_len = max(tmp, max_len)

print(max_len**2)
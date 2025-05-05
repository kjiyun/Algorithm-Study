import sys
input = sys.stdin.readline

n = int(input())
dp = [1e9 for _ in range(n+1)]

dp[n] = 0
for i in range(n, 1, -1):
    if i % 3 == 0: # 3으로 나누어 떨어지는 경우
        dp[i//3] = min(dp[i]+1, dp[i//3])
    if i % 2 == 0:
        dp[i//2] = min(dp[i]+1, dp[i//2])
    dp[i-1] = min(dp[i]+1, dp[i-1])

print(dp[1])
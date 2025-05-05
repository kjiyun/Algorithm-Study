import sys
input = sys.stdin.readline

n = int(input())
plans = []
dp = [0 for _ in range(n+2)]
for _ in range(n):
    t, p = map(int, input().split())
    plans.append((t, p))

# bottom-up 방식
for i in range(1, n+1):
    t, p = plans[i-1]
    dp[i+1] = max(dp[i+1], dp[i])  # 상담을 하지 않은 경우 이익 전파
    if i+t <= n+1:
        dp[i+t] = max(dp[i]+p, dp[i+t])

print(dp[-1])
# 1로 만들기

x = int(input())
dp = [0]*(x+1)

for i in range(2, x+1):
    dp[i] = dp[i-1] + 1 #-1을 먼저 하는 경우
    
    if (i%2==0):
        dp[i] = min(dp[i], dp[i//2]+1)
    if (i%3==0): #2와 3으로 모두 나눠지는 경우, 각각의 연산 횟수의 최소를 비교해야하므로 if문을 2번 사용
        dp[i] = min(dp[i], dp[i//3]+1)

print(dp[x])
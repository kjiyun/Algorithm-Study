# 01 타일

# 메모리 초과 문제 발생
import sys

sysInput = sys.stdin.readline

n = int(sysInput())

d = [0 for _ in range(n+1)]

def seq(n):
    for i in range(n+1):
        if i==1:
            d[i] = 1
        elif i==2:
            d[i] = 2
        else:
            d[i] = d[i-1] + d[i-2]
    return d[n]
    
print(seq(n) % 15476)


#다른 방법
n = int(sysInput())

dp = [0]*(1000001) #(n+1)로 할 경우 런타임에러
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1]+dp[i-2]) % 15746

print(dp[n])
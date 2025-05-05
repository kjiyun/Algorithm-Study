# 해당 번호 내에서 1,2,3 조합할 때 dp를 사용해야 한다고 생각했다.
# 하지만 번호 간에 관계에서 dp를 이용하는 것이 좋다.
# *중요* 4를 표현하는 방법이 7가지일 때, 5를 표현하는 방법은 4에서 +1, 3에서 +2, 2에서 +3을 하는 방법이 있다.

import sys
input = sys.stdin.readline

t = int(input())
n_list = []
dp = [0]*11 # n은 11보다 작아야 함
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(t):
    n = int(input())
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
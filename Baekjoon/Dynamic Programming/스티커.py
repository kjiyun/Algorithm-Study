'''
DP 문제
이 문제의 중요한 포인트는 "n번쨰 열은 반드시 선택해야 한다" 이다.
dp[0][n-1] = dp[1][n-2] + arr[0][n-1]
dp[0][n-1] = dp[1][n-3] + arr[0][n-1]
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    n = int(input())
    arr = [[] for _ in range(2)] # 2행 n열
    dp = [[0]*n for _ in range(2)]

    for i in range(2):
        arr[i] = list(map(int, input().split()))

    # n == 1인 경우
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # n == 2인 경우 -> n == 1인 경우에는 실행하면 안됨
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, n):
        if dp[1][i-1] + arr[0][i] < dp[1][i-2] + arr[0][i]: #최댓값 저장하기
            dp[0][i] = dp[1][i-2] + arr[0][i] 
        else:
            dp[0][i] = dp[1][i-1] + arr[0][i]

        if dp[0][i-1] + arr[1][i] < dp[0][i-2] + arr[1][i]:
            dp[1][i] = dp[0][i-2] + arr[1][i]
        else:
            dp[1][i] = dp[0][i-1] + arr[1][i]
    
    if dp[0][n-1] < dp[1][n-1]:
        print(dp[1][n-1])
    else:
        print(dp[0][n-1])
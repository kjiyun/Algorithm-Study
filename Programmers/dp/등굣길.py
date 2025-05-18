'''
경로의 개수를 세는 문제에서는 모든 경로를 다 탐색할 필요 없이, DP로 누적해나가는 방식이 훨씬 빠름
dp[i][j] = dp[i-1][j] + dp[i][j-1]
'''

def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m]

print(solution(4, 3, [[2, 2]]))

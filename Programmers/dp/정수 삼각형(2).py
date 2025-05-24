def solution(triangle):
    answer = 0
    dp = [[0] for _ in range(len(triangle))]
    for i in range(len(triangle)):
        dp[i] = [0]*(i+1)
    dp[0] = triangle[0]
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            if dp[i+1][j] < dp[i][j] + triangle[i+1][j]:
                dp[i+1][j] = dp[i][j] + triangle[i+1][j]
            if dp[i+1][j+1] < dp[i][j] + triangle[i+1][j+1]:
                dp[i+1][j+1] = dp[i][j] + triangle[i+1][j+1]
    print(dp)
    
    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
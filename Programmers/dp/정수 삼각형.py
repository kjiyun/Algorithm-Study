# DP - bottom up으로 푼 문제
# 값을 차례차례 더해가면서 업데이트하는 방식으로 풀면 된다.

def solution(triangle):
    dp = [0] * len(triangle)
    for i in range(len(triangle)):
        dp[i] = [0] * len(triangle[i])
    
    dp[0] = triangle[0]
    
    for idx in range(1, len(triangle)):
        for k in range(len(triangle[idx])):
            if k == 0:
                dp[idx][k] = dp[idx-1][0] + triangle[idx][k]
            elif k == len(triangle[idx]) - 1:
                dp[idx][k] = dp[idx-1][-1] + triangle[idx][k]
            else:
                if dp[idx-1][k-1] + triangle[idx][k] < dp[idx-1][k] + triangle[idx][k]:
                    dp[idx][k] = dp[idx-1][k] + triangle[idx][k]
                else:
                    dp[idx][k] = dp[idx-1][k-1] + triangle[idx][k]
    
    return max(dp[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
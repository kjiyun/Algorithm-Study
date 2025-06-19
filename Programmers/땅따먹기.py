# DP를 이용하는 문제 -> bottom up
# 완전탐색을 사용하면 4^100000이 되므로 불가능

def solution(land):
    if len(land) == 1:
        return max(*land)
    
    for i in range(1, len(land)):
        for j in range(4):
            now = land[i][j]
            for k in range(4):
                if j == k:
                    continue
                land[i][j] = max(land[i][j], now + land[i-1][k])

    return max(land[-1])

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))
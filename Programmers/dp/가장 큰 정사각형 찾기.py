'''
2차원 DP 문제 (DP라고 생각도 못함..)
DP인 이유 : 작은 정사각형부터 확인하고, 하나하나 키워가면서 확인하는 문제
**점화식**
dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
'''

def solution(board):
    answer = 0
    dp = [[0]*len(board[0]) for _ in range(len(board))]
    
    for i in range(len(board[0])):
        dp[0][i] = board[0][i]
    
    for j in range(len(board)):
        dp[j][0] = board[j][0]
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    max_num, tmp = 0, 0
    for k in range(len(board)):
        tmp = max(dp[k])
        max_num = max(max_num, tmp)
    
    return max_num ** 2
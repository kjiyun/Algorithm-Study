'''
해당 문제에서 가장 중요한 부분은 말을 상, 하, 좌, 우로 이동할 때 장애물이나 벽에 부딪힐 때까지 쭉 미끄러져 이동한다는 점
'''

from collections import deque

def bfs(x, y, board):
    dx = [0,1,0,-1] #우,하,좌,상
    dy = [1,0,-1,0]
    
    queue = deque()
    queue.append((x, y, 0)) #현재위치, 이동횟수
    v = [[0]*len(board[0]) for _ in range(len(board))]
     
    while queue:
        cx, cy, cnt = queue.popleft()

        if board[cx][cy] == 'G':
            return cnt
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            while 0<=nx<len(board) and 0<=ny<len(board[0]) and board[nx][ny] != 'D':
                if 0<=nx+dx[i]<len(board) and 0<=ny+dy[i]<len(board[0]) and board[nx+dx[i]][ny+dy[i]] != 'D':
                    nx += dx[i]  # 동일한 방향으로 이동
                    ny += dy[i]
                else:
                    break
            
            if 0<=nx<len(board) and 0<=ny<len(board[0]) and v[nx][ny] == 0 and board[nx][ny] != 'D':
                v[nx][ny] = 1
                queue.append((nx, ny, cnt+1))
    return -1

def solution(board):
    answer = 0
    
    # 시작, 도착, 장애물 위치 찾기
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                answer = bfs(i, j, board)
    
    return answer
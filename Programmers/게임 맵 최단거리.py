# dfs

# count = 1

# def solution(maps):
#     global count

#     temp = []
#     dx = [0, 1, 0, -1] #동,서,남,북
#     dy = [1, 0, -1, 0]

#     def dfs(x, y):
#         global count
#         maps[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if (nx < len(maps) and ny < len(maps[0]) and nx >= 0 and ny >= 0) and maps[nx][ny]:
#                 count += 1
#                 print("now :",nx, ny)
#                 dfs(nx, ny)
#                 temp.append(count)
#             if nx == len(maps)-1 and ny == len(maps[0])-1: # 맨마지막인 경우 멈춤
#                 break
#         print(temp)
#         # count = temp[0]
            
                

#     dfs(0,0)

#     if maps[-1][-1] == 1:
#         count = -1

#     print(count)
#     return count
from collections import deque
def solution(maps):
    dx = [0, 1, 0, -1] #동,서,남,북
    dy = [1, 0, -1, 0]

    def bfs(x, y):
        queue = deque()
        queue.append((x,y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if (nx < len(maps) and ny < len(maps[0]) and nx >= 0 and ny >= 0) and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
            
        if maps[-1][-1] == 1:
            return -1
        return maps[-1][-1]
    
    bfs(0,0)
    



# maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
solution(maps)

# dfs보다는 bfs가 더 적합한 것 같음

#2번째 풀었을 때
from collections import deque

def solution(maps):
    dx = [0, 1, 0, -1] #행: 우, 하, 좌, 상 (좌표와 행렬 구분 필요)
    dy = [1, 0, -1, 0]
    h = len(maps) # 행의 길이
    w = len(maps[0]) # 열의 길이
    
    def bfs(a, b):
        queue = deque()
        queue.append((a, b))
        
        while queue:
            x, y = queue.popleft() 
            
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if h > nx >= 0 and w > ny >= 0 and maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
    
    bfs(0,0) # (0,0)에서 시작
    
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
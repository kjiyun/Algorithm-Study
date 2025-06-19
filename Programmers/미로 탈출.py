from collections import deque

def bfs(maps, start, finish):
    dx = [0, 1, 0, -1] #우, 하, 좌, 상
    dy = [1, 0, -1, 0]
            
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    queue = deque([start])
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()

        if (x, y) == finish:
            return visited[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and visited[nx][ny] == -1:
                if maps[nx][ny] in {'O', 'L', 'E'}:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return -1

def solution(maps):
    # 시작지점 찾기
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
                
    to_lever = bfs(maps, start, lever)

    if to_lever != -1:
        to_exit = bfs(maps, lever, exit)
    else:
        to_exit = -1
    
    if to_exit != -1:
        return to_lever + to_exit 
    else:
        return -1

maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"]
print(solution(maps))
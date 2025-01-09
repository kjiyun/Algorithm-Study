# 미로 탐색
# bfs 방식 적용
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
result = []
count = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(4):
    graph.append(list(map(int, input().rstrip())))

def bfs(x, y):
    global count

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1
    
    return graph[n-1][m-1]

print(bfs(0, 0))

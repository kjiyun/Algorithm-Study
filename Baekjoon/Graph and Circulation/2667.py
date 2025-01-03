# 단지번호붙이기

# DFS로
# import sys
# input = sys.stdin.readline

# def dfs(x, y):
#     global count

#     if x < 0 or x >= n or y < 0 or y >= n:
#         return 

#     if graph[x][y] == 1: 
#         count += 1
#         graph[x][y] = 0 # 0으로 변경해서 다시 방문하지 않도록 함
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx, ny)

# n = int(input())
# graph = [] # 입력받을 그래프를 담을 리스트 선언
# result = [] # 결과를 담을 리스트 선언
# count = 0

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# for _ in range(n):
#     graph.append(list(map(int, input().rstrip())))


# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             dfs(i, j)
#             result.append(count)
#             count = 0

# result.sort()

# print(len(result))
# for r in result:
#     print(r)

# BFS로
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []  # 입력받을 그래프를 담을 리스트 선언
result = []  # 결과를 담을 리스트 선언

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0
    count = 1  # (x, y)를 방문한 것이므로 1부터 시작

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0  # 방문 처리
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue  # dfs에서는 재귀함수 사용하므로 return 

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                count += 1

    return count

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = bfs(graph, i, j)
            result.append(count)

result.sort()

print(len(result))
for r in result:
    print(r)
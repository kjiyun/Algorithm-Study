#바이러스

#생각정리: dfs또는 bfs 모두 사용가능할 듯

# DFS
import sys
input = sys.stdin.readline

com_n = int(input())
n = int(input())

graph = [[] for _ in range(com_n+1)]  
visited = [False] * (com_n+1) # 방문 정보
count = 0 # 1번 컴퓨터와 연결된 컴퓨터 수

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    global count
    visited[start] = True # 방문 처리

    for i in graph[start]:
        if visited[i] == False: # 방문하지 않은 경우
            count += 1
            dfs(i)

dfs(1)
print(count)

#BFS
from collections import deque
import sys
input = sys.stdin.readline

com_n = int(input())
n = int(input())

graph = [[] for _ in range(com_n+1)]  
visited = [False] * (com_n+1) # 방문 정보
count = 0 # 1번 컴퓨터와 연결된 컴퓨터 수

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    global count
    q = deque([start])
    visited[start] = True

    while q:
        r = q.popleft()
        
        for g in graph[r]:
            if visited[g] == False:
                visited[g] = True
                count += 1
                q.append(g)

bfs(1)
print(count)
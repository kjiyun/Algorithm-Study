# DFS와 BFS

from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)  # 재귀함수 사용하므로
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()  # 오름차순 정렬

def dfs(r):
    visited[r] = True
    print(r, end=" ")

    for g in graph[r]:
        if not visited[g]:
            dfs(g)

def bfs(r):
    queue = deque([r])
    visited[r] = True

    while queue:
        v = queue.popleft()
        print(v, end =" ")
    
        for g in graph[v]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)

visited = [False] * (n+1)
dfs(r)

print()

visited = [False] * (n+1)
bfs(r)
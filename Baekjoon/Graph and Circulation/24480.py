# 알고리즘 수업 - 깊이 우선 탐색 2

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
count = 1

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort(reverse=True) # 내림차순 정렬

def dfs(r):
    global count
    visited[r] = count

    for g in graph[r]:
        if visited[g] == 0:
            count += 1
            dfs(g)

dfs(r)

for v in visited[1:]:
    print(v)
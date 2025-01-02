# 알고리즘 수업 - 깊이 우선 탐색 1

import sys
sys.setrecursionlimit(10 ** 6)  # 재귀를 사용하는 경우
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]  # 입력받은 내용 저장
visited = [0] * (n+1)  # 방문한 노드 기록하는 리스트 생성
count = 1  # 방문 순서 저장하는 변수

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()

def dfs(r):
    global count
    visited[r] = count
        
    for g in graph[r]:
        if visited[g] == 0:  #방문하지 않은 경우
            count += 1
            dfs(g)  # 재귀함수

dfs(r)

for v in visited[1:]:
    print(v)
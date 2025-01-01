# 알고리즘 수업 - 너비 우선 탐색 1

from collections import deque
import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]  # 간선 정보 입력받는 리스트
visited = [0] * (n+1)  # 방문 순서 저장하는 리스트
count = 1  # 방문 순서 기록 변수

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) # 무방향 그래프이므로 양쪽에 추가

def bfs(r):
    global count # 전역변수 설정

    queue = deque([r])
    visited[r] = 1

    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft() # 큐의 왼쪽에 있는 값 가져오기
        graph[v].sort() # 오름차순 정렬

        for g in graph[v]:
            if visited[g] == 0:
                count += 1
                visited[g] = count
                queue.append(g)

bfs(r)

for v in visited[1:]:
    print(v)
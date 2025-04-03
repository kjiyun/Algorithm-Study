# 전력망을 하나씩 끊어봐야함 -> 완전탐색
from collections import deque

def bfs(start, graph, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    cnt = 0

    while queue:
        current = queue.popleft()
        cnt += 1
        for neighbor in graph[current]:
            if visited[neighbor] ==  False:
                visited[neighbor] = True
                queue.append(neighbor)
    return cnt

def solution(n, wires):
    min_diff = float('inf') # 최소를 구해야하므로 +inf

    for i in range(len(wires)):
        # 트리 형태 간선 더하기
        graph = {k:[] for k in range(1, n+1)}
        visited = [False]*(n+1)

        for j, (v1, v2) in enumerate(wires):
            if i==j: # 끊는 간선을 의미
                continue
            else:
                graph[v1].append(v2)
                graph[v2].append(v1)
        one = bfs(1, graph, visited)
        two = n-one
        min_diff = min(min_diff, abs(one-two))
    return min_diff

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))
'''
내가 푼 방식:
    최단 거리를 구하는 문제이므로 bfs를 사용하는 방식을 생각했음
    먼저 road에 있는 정보를 graph 이차원 배열에 저장하고,
    1에서 출발하는 것으로 고정되어 있으므로 1부터 시작해서 다음에 이동할 값을 queue에 넣고
    하나씩 순차로 이동하는 방식 적용

다른 사람이 푼 방식:
    **다익스트라 방식 사용
'''

### 다익스트라 방식
import heapq

def dijkstra(dist, adj):
    heap = []
    heapq.heappush(heap, [0, 1]) # [거리, 노드]
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(heap, [cost+c, n])

def solution(N, road, K):
    dist = [float('inf')]*(N+1)
    dist[1] = 0
    adj = [[] for _ in range(N+1)]
    for r in road:
        adj[r[0]].append(r[2], r[1])
        adj[r[1]].append(r[2], r[0])
    dijkstra(dist, adj)
    return len([i for i in dist if i <=K])


### 내가 푼 방식
from collections import deque

def solution(N, road, K):
    global answer
    graph = [[0]*(N+1) for _ in range(N+1)]
    deliver = [0]*(N+1)
    
    # 최소 경로 찾기 -> BFS
    for r in road:
        if graph[r[0]][r[1]] > 0 and graph[r[0]][r[1]] < r[2]:
            continue
        graph[r[0]][r[1]] = r[2]
        graph[r[1]][r[0]] = r[2]
    
    def bfs(start):
        global answer
        answer = 0
        queue = deque()
        queue.append(start)
        
        while queue:
            x = queue.popleft()
            
            for i in range(2, N+1):
                c = graph[x][i]
                if c > 0 and deliver[i] > deliver[x] + c:
                    deliver[i] = (deliver[x] + c)
                    queue.append(i)
                elif c > 0 and deliver[i] == 0:
                    deliver[i] = (deliver[x] + c)
                    queue.append(i)
                    
        for k in range(1, len(deliver)):
            if deliver[k] <= K:
                answer += 1
    
    bfs(1)

    return answer
def solution(n, computers):
    
    def dfs(v):
        visited[v] = True

        for nei in range(n):
            if not visited[nei] and computers[v][nei]:
                dfs(nei)

    count = 0
    visited = [False] * n # 모든 노드를 방문하지 않은 노드라고 간주
    
    for i in range(n):
        if not visited[i]: #방문하지 않은 노드인 경우
            dfs(i)
            count += 1
    return count


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]] # n*n 형태
solution(n, computers)
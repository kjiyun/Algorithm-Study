'''
DFS와 BFS를 모두 사용한 문제
1. 7명을 선택하기 (DFS 사용) -> 2차원 배열을 1차원으로 취급해서 [n//5][n%5] 로 진행
2. 7명인지, 다솜파가 4명 이상인지 체크
3. BFS로 선택한 인원의 인접여부 판단 (check 함수)
4. 인접한 경우 answer += 1
'''

from collections import deque

def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited = [[False]*5 for _ in range(5)]

    dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]
    cnt = 1
    visited[a][b] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and v[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt == 7

    
def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1:
                return bfs(i, j)

def dfs(n, cnt, scnt):
    global answer
    if cnt>7:                   # 가지치기: 이미 7명을 넘었으면 7공주 불가!
        return

    if n == 25:
        if cnt == 7 and scnt >= 4:
            if check(): # 인접 여부 체크
                answer += 1
        return  # n==25인 경우는 리턴
    
    v[n//5][n%5] = 1  # 포함하는 경우
    dfs(n+1, cnt+1, scnt+int(arr[n//5][n%5] == 'S'))
    v[n//5][n%5] = 0  # 원상복구
    dfs(n+1, cnt, scnt)


arr = []
answer = 0
for _ in range(5):
    arr.append(list(map(str, input().rstrip())))
v = [[0]*5 for _ in range(5)]

dfs(0, 0, 0) # 학생 번호, 포함 학생 수, 다솜파 학생 수
print(answer)
# 플로이드

n = int(input()) # n개의 도시
m = int(input()) # m개의 버스
INF = int(1e9)  # 1e9 == 정수형으로 10억
P = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    P[a][b] = min(P[a][b], c)

for i in range(1, n+1):
    P[i][i] = 0

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            P[a][b] = min(P[a][b], P[a][k] + P[k][b])

for x in range(1, n+1):
    for y in range(1, n+1):
        if P[x][y] == INF:
            print(0, end=' ')
        else:
            print(P[x][y], end=' ')
    print()
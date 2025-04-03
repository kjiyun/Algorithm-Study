import sys, copy
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

dir = [(0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

new_nutri = [((n-1), 0), ((n-2), 0), ((n-1), 1), ((n-2), 1)]

for _ in range(m):
    d, p = map(int, input().split()) #이동 방향과 이동 칸 수

    nutrients = copy.deepcopy(new_nutri)
    new_nutri.clear()
    # 1. 영양제 이동
    for k in range(len(nutrients)):
        x = (nutrients[k][0] + dir[d-1][0]*p)%n
        y = (nutrients[k][1] + dir[d-1][1]*p)%n

        # 2. 영양제 투입 후 삭제
        print("x, y:",x,y)
        arr[x][y] += 1
        nutrients[k] = (x, y)
    
    for a in nutrients:
        if 0<=(a[0]-1)<n and 0<=(a[1]-1)<n and arr[a[0]-1][a[1]-1] != 0:
            arr[a[0]][a[1]] += 1

        if 0<=(a[0]-1)<n and 0<=(a[1]+1)<n and arr[a[0]-1][a[1]+1] != 0:
            arr[a[0]][a[1]] += 1

        if 0<=(a[0]+1)<n and 0<=(a[1]-1)<n and arr[a[0]+1][a[1]-1] != 0:
            arr[a[0]][a[1]] += 1

        if 0<=(a[0]+1)<n and 0<=(a[1]+1)<n and arr[a[0]+1][a[1]+1] != 0:
            arr[a[0]][a[1]] += 1
    
    for i in range(n):
        for j in range(n):
            if (i, j) not in nutrients and arr[i][j] >= 2:
                arr[i][j] -= 2
                # 영양제 위치 저장
                new_nutri.append((i, j))

sum = 0
for i in range(n):
    for j in range(n):
        sum += arr[i][j]
print(sum)
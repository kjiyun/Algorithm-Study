# def solution(n):
#     answer = [[0]*n for _ in range(n)]
#     mode = 'r'
#     x = 0
#     y = 0
#     for i in range(n*n):
#         answer[x][y] = i+1
#         if mode == 'r':
#             y += 1
#             if y == n-1 or answer[x][y+1] != 0: 
#                 mode = 'd' #아래로 이동
#         elif mode == 'd':
#             x += 1
#             if x == n-1 or answer[x+1][y] != 0:
#                 mode = 'l' #왼쪽으로 이동
#         elif mode == 'l':
#             y -= 1
#             if y == 0 or answer[x][y-1] != 0:
#                 mode = 'u' #위로 이동
#         elif mode == 'u':
#             x -= 1
#             if x == 0 or answer[x-1][y] != 0:
#                 mode = 'r'
#     print(answer)

def solution(n):
    answer = [[0]*n for _ in range(n)]
    dx = [0,1,0,-1] # 우, 하, 좌, 상
    dy = [1,0,-1,0]
    x = 0
    y = 0

    answer[x][y] = 1
    k = 2
    while k <= (n*n):
        for i in range(4):
            while True:
                nx = x + dx[i]
                ny = y + dy[i]
            
                if nx >= n or ny >= n or nx < 0 or ny < 0 or answer[nx][ny]!=0:
                    break
                else:
                    answer[nx][ny] = k
                    x = nx
                    y = ny
                    k += 1
            
    print(answer)

n = 5
solution(n)
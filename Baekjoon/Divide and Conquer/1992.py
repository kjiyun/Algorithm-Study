# 쿼드트리

n = int(input())
video = [[0]*n for _ in range(n)]

for i in range(n):
    video[i] = list(map(int, input()))

def condense_video(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if video[x][y] != video[i][j]:  #범위 안에 한개라도 다른 경우에는 4분면으로 나눠서 다시 검색한다.
                print("(", end="")  #4분면으로 나눌 경우 괄호를 친다.
                condense_video(x, y, n//2)
                condense_video(x, y+n//2, n//2)
                condense_video(x+n//2, y, n//2)
                condense_video(x+n//2, y+n//2, n//2)
                print(")", end="")
                return 
            
    print(1 if video[x][y] == 1 else 0, end="")

condense_video(0, 0, n)
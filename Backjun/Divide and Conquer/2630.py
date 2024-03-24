# 색종이 만들기

n = int(input())
color_paper = [[0]*n for _ in range(n)]

for i in range(n):
    color_paper[i] = list(map(int, input().split()))

white_count = 0 #흰 색종이 게수
blue_count = 0 #파란 색종이 개수

def make_color_paper(num, paper):
    global white_count
    global blue_count
    check = 0 # 색종이가 만들어지는 여부 확인

    for i in range(num):
        check += sum(paper[i])
    if check == 0:
        white_count += 1
    elif check == num*num:
        blue_count += 1
    else:
        new_size = num // 2

        temp = [paper[i][:new_size] for i in range(0, new_size)]
        make_color_paper(new_size, temp)

        temp = [paper[i][:new_size] for i in range(new_size, num)]
        make_color_paper(new_size, temp)

        temp = [paper[i][new_size:num] for i in range(0, new_size)]
        make_color_paper(new_size, temp)

        temp = [paper[i][new_size:num] for i in range(new_size, num)]
        make_color_paper(new_size, temp)

make_color_paper(n, color_paper)
print(white_count)
print(blue_count)


# 다른 방법
import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []

def solution(x, y, N):
    color = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if color != paper[i][j]:
                solution(x, y, N//2)
                solution(x, y+N//2, N//2)
                solution(x+N//2, y, N//2)
                solution(x+N//2, y+N//2, N//2)
    if color == 0:
        result.append(0)
    else:
        result.append(1)

solution(0,0,N)
print(result.count(0))
print(result.count(1))
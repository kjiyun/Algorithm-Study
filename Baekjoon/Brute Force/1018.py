#체스판 다시 칠하기

#틀린 방식 : 이 방식은 8x8 크기의 체스판으로 잘라내는 과정이 없음 + 다시 칠해야 하는 정사각형의 최소를 구하는 것이 아님
n, m = map(int, input().split())
chess = []
result = 0

for _ in range(n):
    chess.append(input())

for i in range(n):
    for j in range(m):
        if chess[0][0] == 'W':
            if i%2 == 0 and j%2 == 0 and chess[i][j] == 'B':
                result += 1
            elif i%2 == 1 and j%2 == 1 and chess[i][j] == 'B':
                result += 1
            elif i%2 == 1 and j%2 == 0 and chess[i][j] == 'W':
                result += 1
            elif i%2 == 0 and j%2 == 1 and chess[i][j] == 'W':
                result += 1
        
        elif chess[0][0] == 'B':
            if i%2 == 0 and j%2 == 0 and chess[i][j] == 'W':
                result += 1
            elif i%2 == 1 and j%2 == 1 and chess[i][j] == 'W':
                result += 1
            elif i%2 == 1 and j%2 == 0 and chess[i][j] == 'B':
                result += 1
            elif i%2 == 0 and j%2 == 1 and chess[i][j] == 'B':
                result += 1

print(result)

# 올바른 방법
n,m = map(int, input().split())
original = []
count = []

for _ in range(n):
    original.append(input())

#전체 체스판에서 시작점을 잡기 위한 반복문
for a in range(n-7):
    for b in range(m-7):
        index1 = 0 #'W'로 시작할 경우 바뀐 체스판의 갯수 세기 위함
        index2 = 0 #'B'로 시작할 경우 바뀐 체스판의 갯수 세기 위함
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0: #합이 짝수일 경우
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))
print(min(count))
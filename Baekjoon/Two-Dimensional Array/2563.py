#색종이**

#겹치는 부분의 넓이를 찾는 것이 중요
n = int(input())  #색종이의 수
paper = [[0]*100 for _ in range(100)]  #도화지 영역

for i in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

result = 0  #넓이 출력
for k in range(100):
    result += paper[k].count(1)  #값이 1인 부분의 수를 출력

print(result)
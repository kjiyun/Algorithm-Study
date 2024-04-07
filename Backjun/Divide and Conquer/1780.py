# 종이의 개수

n = int(input())

paper = [[0]*n for _ in range(n)]

for i in range(n):
    paper[i] = list(map(int, input().split()))

result = {-1:0, 0:0, 1:0}

def num_paper(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[x][y] != paper[i][j]:  #여기서 막혔다. 값이 같은 경우에는 다시 for문을 도는 것이므로 고려할 필요 없음 
                next = n//3
                num_paper(x, y, next)
                num_paper(x, y+next, next)
                num_paper(x, y+next*2, next)
                num_paper(x+next, y, next)
                num_paper(x+next*2, y, next)
                num_paper(x+next, y+next, next)
                num_paper(x+next, y+next*2, next)
                num_paper(x+next*2, y+next, next)
                num_paper(x+next*2, y+next*2, next)
                return 
    result[paper[x][y]] += 1

num_paper(0,0,n)

for i in result.values():
    print(i)
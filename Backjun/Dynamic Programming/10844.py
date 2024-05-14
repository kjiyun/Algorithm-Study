# 쉬운 계단 수

# a[n][k] : n은 자리 수, k는 마지막 자리의 숫자

n = int(input())
a = [[0]*10 for _ in range(n+1)] #개수를 저장 

# 한 자리인 경우
for i in range(1, 10):
    a[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if (j==0):
            a[i][0] = a[i-1][1]
        elif(j==9):
            a[i][9] = a[i-1][8]
        else:
            a[i][j] = a[i-1][j-1] + a[i-1][j+1]

print(sum(a[n])%1000000000)
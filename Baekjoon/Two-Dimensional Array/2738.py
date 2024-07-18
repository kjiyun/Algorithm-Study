#행렬 덧셈

#런타임에러
n, m = map(int, input().split())

array1 = [[0]*n for _ in range(m)]
array2 = [[0]*n for _ in range(m)]

for i in range(n):
    array1[i] = list(map(int, input().split()))

for i in range(n):
    array2[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        print(array1[i][j] + array2[i][j], end=' ')
    print()

#올바른 방법
n, m = map(int, input().split())

A, B = [], []

for i in range(n):
    a = list(map(int, input().split()))
    A.append(a)

for i in range(n):
    b = list(map(int, input().split()))
    B.append(b)

for i in range(n):
    for j in range(m):
        print(A[i][j] + B[i][j], end=' ')
    print()
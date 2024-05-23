# 회의실 배정

n = int(input())
arr = [[0]*n]*n

for i in range(n):
    arr[i] = list(map(int, input().split()))
print(arr)

sum = 1
num = []
for i in range(1, n):
    if arr[i-1][1] <= arr[i][0]:
        sum = 1
    else:
        min = arr[i-1][1]
print(num)
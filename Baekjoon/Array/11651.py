#좌표 정렬하기2

import sys

n = int(sys.stdin.readline())
arr = [[0]*2 for _ in range(n)]

for i in range(n):
    arr[i] = list(map(int, sys.stdin.readline().split()))

arr.sort(key=lambda x : (x[1], x[0]))

for d in arr:
	print(d[0], d[1])
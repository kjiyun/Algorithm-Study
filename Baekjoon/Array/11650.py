#좌표 정렬하기
import sys

n = int(sys.stdin.readline())
arr = [[0]*2 for _ in range(n)]

for i in range(n):
    arr[i][0], arr[i][1] = map(int, sys.stdin.readline().split())

arr.sort()
for i in range(len(arr)):
    print(arr[i][0], arr[i][1])
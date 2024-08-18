#수 정렬하기 3
#수 정렬하기2(2751)과 같은 방식으로 하는 경우 메모리 초과
import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()
for i in arr:
    print(i)

#올바른 방법: 계수 정렬 사용
import sys

n = int(sys.stdin.readline())
arr = [0] * (10000 + 1)

for i in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(len(arr)):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
# 수 정렬하기 2
import sys

n = int(sys.stdin.readline())
n_list = [0]*n
for i in range(n):
    n_list[i] += int(sys.stdin.readline())

n_list.sort()
for i in n_list:
    print(i)
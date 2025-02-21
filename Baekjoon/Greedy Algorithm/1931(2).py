# 회의실 배정

import sys
input = sys.stdin.readline


n = int(input()) # 회의의 수

arr = []

for _ in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))
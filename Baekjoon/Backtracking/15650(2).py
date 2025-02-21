# N과 M (2)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def bt(start):
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(start, n+1):
        if i not in arr:
            arr.append(i)
            bt(i+1)
            arr.pop()

bt(1)
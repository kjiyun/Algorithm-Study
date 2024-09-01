#N과 M(4)

import sys
input = sys.stdin.readline()

def dfs(start):
    if len(array) == m:
        print(" ".join(map(str, array)))
        return
    for i in range(start,n+1):
        array.append(i)
        dfs(i)
        array.pop()

n, m = map(int, input.split())
array = []
dfs(1)
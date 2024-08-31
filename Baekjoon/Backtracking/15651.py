#N과 M (3)

import sys
input = sys.stdin.readline()

def dfs():
    if len(array) == m:
        print(" ".join(map(str, array)))
        return
    for i in range(1,n+1):
        array.append(i)
        dfs()
        array.pop()

n, m = map(int, input.split())
array = []
dfs()
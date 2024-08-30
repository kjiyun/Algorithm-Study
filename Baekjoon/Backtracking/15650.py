#N과 M(2)

import sys
input = sys.stdin.readline()

def dfs(start):
    if len(array) == m:
        print(" ".join(map(str, array)))
        return
    for i in range(start, n+1):
        if i not in array:
            array.append(i)
            dfs(i+1)
            array.pop()        

n, m = map(int, input.split())
array = []
dfs(1)
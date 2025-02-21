# N과 M (1)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def bt():
    if len(arr) == m:
        print(*arr) # * 하면 [ ] 없어짐
        return 
    
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            bt()
            arr.pop()

bt()
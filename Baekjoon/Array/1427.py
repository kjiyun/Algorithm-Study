#소트인사이드
import sys

n = list(sys.stdin.readline())

n.sort(reverse=True)
for i in n:
    print(i, end='')

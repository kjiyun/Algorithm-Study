# 최소 힙

import sys, heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())

    if (x != 0):
        heapq.heappush(heap, x)
    else:
        try:
            print(heapq.heappop(heap))  # heap에서 최소를 출력한다는 의미
        except:
            print(0)
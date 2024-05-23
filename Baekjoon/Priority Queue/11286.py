# 절댓값 힙

import sys, heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    
    if x != 0:
        #abs(x)는 x의 절댓값을 의미, tuple로 하는 경우 tuple의 0번째 인덱스가 우선순위가 된다.
        heapq.heappush(heap, (abs(x), x))  
    else:
        try:
            print(heapq.heappop(heap)[1]) #pop하는 경우, tuple의 두번째 값(원래 값) 출력
        except:
            print(0)
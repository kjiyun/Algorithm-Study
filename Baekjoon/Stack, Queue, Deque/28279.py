# 덱 2
import sys
from collections import deque

n = int(sys.stdin.readline())
deq = deque([]) 

for _ in range(n):
    # cmd = sys.stdin.readline().split()  이렇게 하면 값을 정수로 변경하지 않고 문자로 인식함
    cmd = list(map(int, sys.stdin.readline().split()))

    if cmd[0] == 1:
        deq.appendleft(cmd[1])
    elif cmd[0] == 2:
        deq.append(cmd[1])
    elif cmd[0] == 3:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif cmd[0] == 4:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif cmd[0] == 5:
        print(len(deq))
    elif cmd[0] == 6:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 7:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif cmd[0] == 8:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
# 큐2
import sys

#시간 초과 문제
#이유: 리스트로 선언해서 pop(0)를 하게 되면, 
#첫 번째 요소를 pop 하고나서 나머지 요소들의 인덱스를 1칸씩 당기는 과정에서 O(n)의 계산량이 발생하기 때문

n = int(sys.stdin.readline()) #명령어 개수
queue = []

for _ in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(queue) == 0:
            print('-1')
        else:
            queue.pop(0)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
    elif cmd[0] == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    elif cmd[0] == 'back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[len(queue)-1])

#deque를 이용하여 시간초과 문제 해결
import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])

for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':  #오른쪽 값을 제거
        if len(queue) == 0:
            print('-1')
        else:
            print(queue.popleft())  #pop(0) 대신 popleft() 사용
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
    elif cmd[0] == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])
    elif cmd[0] == 'back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])
#스택 2

# int(input())으로 입력을 받을 경우 시간 초과 문제 발생
import sys

n = int(sys.stdin.readline()) #명령의 수 
stack = []
k = []

for _ in range(n):
    k = sys.stdin.readline().split()  #리스트로 저장됨
    if k[0] == '1':
        stack.append(k[1])
    elif k[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print('-1')
    elif k[0] == '3':
        print(len(stack))
    elif k[0] == '4':
        if stack:
            print('0')
        else:
            print('1')
    elif k[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print('-1')
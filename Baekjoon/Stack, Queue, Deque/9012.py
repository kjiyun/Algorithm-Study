#괄호

t = int(input())

for _ in range(t):
    stack = []
    n = list(input())
    for i in n:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if not stack:  #스택이 비어있는 경우
            print('YES')
        else:
            print('NO')
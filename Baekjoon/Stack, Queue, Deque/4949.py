#균형잡힌 세상

while True:
    # word = sys.stdin.readline()  개행문자를 포함하므로 '.'만을 판별할 수 없음
    word = input() 
    stack = [] 
    if word == '.':
        break
    for i in word:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':  #()를 만족하는 경우 스택에서 빼기
                stack.pop()
            else:
                stack.append(i)  #()를 만족하지 않는 경우 no 출력 후 다음 입력 받기
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)
                break

    if len(stack) == 0:
        print('yes')
    else:
        print('no')
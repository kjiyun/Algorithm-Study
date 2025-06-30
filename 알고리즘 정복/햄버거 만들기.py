# 하나씩 받을 때마다 최근 4개 확인

def solution(ingredient):
    answer = 0
    stack = []
    
    for i in ingredient:
        if stack and i == 1 and stack[-3:] == [1,2,3]:
            for _ in range(3):
                stack.pop()  # li = li[:-4] -> 깊은 복사이므로 시간 초과 발생
            answer += 1 
            continue
        stack.append(i)
    return answer
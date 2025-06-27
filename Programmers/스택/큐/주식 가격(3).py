def solution(prices):
    answer = [0]*len(prices)
    stack = []

    for i in range(len(prices)):
        while stack and prices[i] < stack[-1][1]: # 스택의 top보다 수가 작은 경우
            idx, p = stack.pop()
            answer[idx] = i - idx
        stack.append((i, prices[i]))
    
    # 순회하고 stack에 남은 수 정리
    for i, _ in stack:
        answer[i] = stack[-1][0] - i
    
    return answer

print(solution([1, 2, 3, 1, 3]))
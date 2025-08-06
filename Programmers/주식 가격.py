def solution(prices):
    answer = [0]*len(prices)
    
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] < stack[-1][1]:
            ti, tp = stack.pop()
            answer[ti] = i - ti
        stack.append((i, prices[i]))

    for si, _ in stack:
        answer[si] = len(prices) - si - 1
    
    return answer
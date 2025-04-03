def solution(prices):
    stack = []
    answer = [0]*len(prices)
    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            answer[stack[-1]] = idx-stack[-1]
            stack.pop()
        stack.append(idx)
    if stack:
        for i in range(len(stack)):
            answer[stack[i]] = stack[-1] - stack[i]
    return answer

prices = [1, 2, 3, 2, 3]
print(solution(prices))
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

# ------------
# 예제에서의 4초 시점과 5초 시점을 어떻게 해야하나 ㅜㅜ
# 가격이 떨어지는 순간 → 지금까지 버틴 시간 = (현재 인덱스 - 시작 인덱스)
# 끝까지 가격이 안 떨어졌다면 → (끝 인덱스 - 시작 인덱스)

def solution(prices):
    answer = [0] * len(prices)
    stack = [[0, prices[0]]]
        
    for i in range(1, len(prices)):
        cnt = 0
        while len(stack) >= 1 and stack[-1][1] > prices[i]:
            idx, price = stack.pop()
            answer[idx] = i - idx
            # print('answer', answer)
        stack.append([i, prices[i]])
        # print('stack', stack)
    
    for j in range(len(stack)):
        idx, price = stack[j]
        # print("idx", idx, price)
        answer[idx] += len(prices) - 1 - idx

    return answer
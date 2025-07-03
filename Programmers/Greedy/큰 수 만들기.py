def solution(number, k):
    answer = ''
    stack = []

    cnt = 0
    for n in number:
        n = int(n)
        while stack and stack[-1] < n and cnt < k: # 넣으려는 값이 더 큰 경우
            stack.pop()
            cnt += 1 # 제거한 횟수 계산

        stack.append(n)

    if k - cnt > 0:
        stack = stack[:-(k-cnt)]

    for s in stack:
        answer += str(s)

    return answer

print(solution("1924", 2))
print(solution("4177252841", 4))
# dfs를 이용한 풀이
def dfs(numbers, target, depth, total):
    global cnt

    if depth == len(numbers) and total == target:
        cnt += 1
        return 

    elif depth == len(numbers):
        return
    
    dfs(numbers, target, depth+1, total + numbers[depth])
    dfs(numbers, target, depth+1, total - numbers[depth])

def solution(numbers, target):
    global cnt
    dfs(numbers, target, 0, 0)

    print(cnt)
    return cnt

numbers = [4,1,2,1]
target = 4
cnt = 0

# 다른 사람 정답
def solution(numbers, target):
    if not numbers and target == 0: # numbers가 비어있고 tartget이 0인 경우 cnt += 1
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
    
print(solution(numbers, target))
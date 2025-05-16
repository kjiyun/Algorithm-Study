# 총 경우가 2^n이라서 모든 경우를 탐색해도 됨
import sys
sys.setrecursionlimit(10**6)

def solution(numbers, target):
    global result
    index = 0
    result = 0  # dfs 함수 내에서 정의하면 dfs 재귀 호출이 될 때마다 초기화되므로 외부에서 초기화

    def dfs(index, current_sum):
        global result  # result함수는 초기화되면 안되므로 외부에 선언 후 global 변수로 선언

        if index == len(numbers) and current_sum == target:  
            result += 1
            return

        if index == len(numbers):
            return 
        
        else:
            if index < len(numbers):
                dfs(index+1, current_sum+numbers[index])
                dfs(index+1, current_sum-numbers[index])
    
    dfs(0, 0)

    return result

print(solution([1, 1, 1, 1, 1], 3))
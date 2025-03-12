# 일정한 크기의 윈도우를 배열이나 리스트 위에서 이동시키며 문제를 해결하는 기법
# 주로 연속된 부분 배열에서 최대/최소값, 특정 조건을 만족하는 구간 등을 찾는 데 사용됨

# 최대 부분 합
# 연속된 부분 배열의 합 중 최대값을 구하라
def solution(nums, k):
    max_sum = float('-inf')
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        if (i >= k-1):
            max_sum = max(max_sum, current_sum)
            current_sum -= nums[i-(k-1)]
    
    return max_sum

# 예시 실행
nums = [2, 1, 5, 1, 3, 2]
k = 3
print(solution(nums, k))  # 출력: 9 (부분 배열 [5, 1, 3])
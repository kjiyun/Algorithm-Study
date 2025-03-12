# 두 수의 합
# 정렬된 배열에서 두 수의 합이 특정 값이 되는 인덱스 쌍 찾기
# 시간 복잡도 : O(n)

def two_sum(nums, target):
    left, right = 0, len(nums) - 1 #left, right가 포인터가 되는 것

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

# 예시 실행
nums = [1, 2, 3, 4, 6]
target = 6
print(two_sum(nums, target))  # 출력: (1, 3)
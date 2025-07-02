'''
시간초과가 안나게 푸는 게 중요한 문제

'''
from collections import Counter
def solution(topping):
    answer = 0
    right_dict = Counter(topping)

    left_dict = {}

    for i in topping:
        
        if i in left_dict:
            left_dict[i] += 1
        else:
            left_dict[i] = 1
        right_dict[i] -= 1

        if right_dict[i] == 0:
            right_dict.pop(i)

        if len(left_dict) == len(right_dict):
            answer += 1
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
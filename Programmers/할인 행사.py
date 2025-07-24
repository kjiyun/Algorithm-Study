from collections import deque, Counter

def solution(want, number, discount):
    answer = 0
    total = sum(number)
    for i in range(len(discount)-total+1):
        cnt = 0
        for fruit, num in zip(want, number):
            # print("fruit:", fruit)
            tmp = discount[i:i+total]
            if tmp.count(fruit) == num:
                cnt += 1
                continue
            else:
                break
        if cnt == len(want):
            answer += 1
    
    return answer

def solution(want, number, discount):
    answer = 0
    # stuff = deque()
    dic1 = dict(zip(want, number))

    for i in range(len(discount)-9):
        window = discount[i:i+10]
        window_count = Counter(window)
        print("window_count", window_count)
        print("dic1", dic1)
        if window_count == dic1: # 딕셔너리는 순서 상관없음
            answer += 1
        print(answer)
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
solution(want, number, discount)
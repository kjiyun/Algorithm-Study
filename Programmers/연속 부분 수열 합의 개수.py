from collections import defaultdict, deque

def solution(elements):
    sum_dict = defaultdict(int) # 0으로 초기화됨
    # sum = 0 # 부분 수열의 합
    current_list = deque()

    for i in range(1, len(elements)+1): #부분 수열의 길이 지정
        cnt = 0
        current_list.clear()
        for j in range(len(elements)*2): #슬라이딩 윈도우 적용 (부분 수열의 길이만큼)
            if j > len(elements)-1:
                j = j - len(elements)
                cnt += 1
            current_list.append(elements[j])
            print("iii:", current_list)
            # sum += elements[left]

            if j >= i-1 or cnt > 0: # 부분 수열의 길이보다 긴 경우
                print("kk", j)
                sum_dict[sum(current_list)] += 1
                current_list.popleft()
                print("cccc", current_list)
        print("sum:", sum_dict)

                
    return len(sum_dict)

elements = [7,9,1,1,4]
print(solution(elements))
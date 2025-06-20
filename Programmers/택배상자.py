def solution(order):
    answer = 0
    i, j = 0, 1
    sub_belt = [] # 보조 컨테이어 벨트
    while i < len(order):
        if j <= len(order) and order[i] == j:
            answer += 1
            i += 1
            j += 1
        elif len(sub_belt) > 0 and sub_belt[-1] == order[i]: # 보조 컨테이너에서 가져올 수 있는 경우
                sub_belt.pop()
                i += 1
                answer += 1
        elif j <= len(order): # j는 1부터 시작하는 것에 유의!
            sub_belt.append(j)
            j += 1

        else:
            break

    return answer
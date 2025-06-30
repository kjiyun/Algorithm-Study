def solution(routes):
    answer = 0

    # 시작이 낮은 순으로 정렬
    # 끝나는 시간이 동일하면 시작하는 시간이 빠른 순서
    routes.sort(key=lambda x:(x[1], x[0]))

    # 처음 카메라는 무조건 있어야 함
    answer += 1

    # 끝나는 시간 세팅
    end = routes[0][1]

    for i in range(1, len(routes)):
        # 초과하면 +1
        if end < routes[i][0]:
            answer += 1
            #  새롭게 이용 가능한 카메라의 끝나는 시간으로 다시 세팅
            end = routes[i][1]

    return answer
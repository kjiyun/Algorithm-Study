def solution(park, routes):
    dx_dict = {'E':0, 'W':0, 'S':1, 'N':-1}
    dy_dict = {'E':1, 'W':-1, 'S':0, 'N':0}

    # 시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x = i
                y = j
    
    for route in routes:
        direction, num = route.split()

        nx = x
        ny = y
        valid = True

        for i in range(int(num)):
            # x, y는 현재 위치
            nx += dx_dict[direction]
            ny += dy_dict[direction]

            if nx >= len(park) or ny >= len(park[0]) or nx < 0 or ny < 0 or park[nx][ny] == 'X':
                valid = False
                print(i)
                break

        if valid == True:    
            x = nx
            y = ny
        

    return [x, y]

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]
print(solution(park, routes))

# 문제점1: return 할 때 [0,1] 형태로 어떻게 출력하는가 -> 해결
# 문제점2: 이동 중간에 장애물을 만나면 다시 원래 위치로 돌아가야함 -> 현재 방식으로는 멈춘 위치가 저장됨 -> 해결
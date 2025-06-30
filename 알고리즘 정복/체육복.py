'''
**다시 풀기**
여유있는 학생은 내가 도난 당했다면 자신을 빌려주기
앞뒤를 살피며 도난 당했다면 빌려줌
왼쪽에서 오른쪽으로 검색을 한다면, 왼쪽을 먼저 빌려줌
'''

def solution(n, lost, reserve):
    answer = 0
    
    # 체육복(전체 인원 모두 가져옴)
    std = [1] * (n+1)
    # 도난 당한 학생 (0으로 표시)
    for i in lost:
        std[i] = 0
    # 여유있는 학생의 데이터는 사실 정렬된 데이터가 아니다
    reserve.sort()
    
    # 여유 있는 학생
    for i in reserve:
        # 내가 도난 당했다면 내가 나를 빌려줘
        if i in lost: #여유 있게 가지고 온 학생이 잃어버린 명단에 있다면
            std[i] = 1
            continue
        # 앞뒤를 살피며 도난 당했다면 빌려줌
        # 왼쪽에서 오른쪽으로 검색을 한다면
        if std[i-1] == 0: # 범위를 확인!!!!
            # (왼쪽을 먼저 빌려줌)
            std[i-1] = 1
            continue
        if i+1 <= n and std[i+1] == 0: # 범위를 확인!!!!
            std[i+1] = 1
    #최종 체육이 가능 한 학생은 몇명일까요?
    answer = n-std.count(0) # 전체 인원 - 잃어버린 학생 수
    return answer
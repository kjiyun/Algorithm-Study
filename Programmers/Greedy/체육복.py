# 

def solution(n, lost, reserve):
    answer = 0
    # 같은 번호가 있다면 제외하기
    lost_set = sorted(set(lost) - set(reserve))
    reserve_set = sorted(set(reserve) - set(lost))

    for r in reserve_set:
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)
    return n - len(lost_set)
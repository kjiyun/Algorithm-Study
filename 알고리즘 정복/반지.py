# 정답!

def solution(wordfind, N, ring):
    answer = 0

    dring = ''
    for i in range(N):
        dring = ring[i] + ring[i]  # 두바퀴 돌림
        if wordfind in dring:
            answer += 1
            
    return answer
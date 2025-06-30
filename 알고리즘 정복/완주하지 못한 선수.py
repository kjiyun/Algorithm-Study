'''
참가자 명단을 dict 형태로 만들고 완주자 명단을 한명씩 빼기
남은 인원이 1명인 경우 return

해시 테이블 자료구조:
    검색이 빠르다.
    중복이 허용되지 않는다.
'''

from collections import Counter

def solution(participant, completion):
    answer = ''
    participant = Counter(participant)
    for c in completion:
        participant[c] -= 1
    for p, n in participant.items():
        if n == 1:
            answer += p
    return answer


### 다른 풀이
def solution(participant, completion):
    answer = ''

    # 참가자 명단 정리
    part = {}

    for i in participant:
        if i in part:
            part[i] += 1
        else:
            part[i] = 1
    
    # 완주자 명단으로 참가자 명단에서 제외
    for i in completion:
        part[i] -= 1
        if part[i] == 0:
            del part[i]

    # 딕셔너리를 리스트로 변환하면 key값만 남음
    answer = list(part)    
    answer = answer[0]
    return answer
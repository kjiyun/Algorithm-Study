'''
**다시 풀기**
풀이 방법:
    1) 나를 기준으로 나보다 큰 점수를 만날 때마다 +1
    2) 정렬한 뒤에 나의 위치가 어디인지 확인 (.index()이용)
'''

def solution(score):
    answer = []
    avg = []

    for i, j in score:
        avg.append((i+j)/2) # 평균을 구하지 않고 더하기만으로 비교해도 됨
    
    avgsort = sorted(avg, reverse=True) # 내림차순으로 정렬한 리스트
    
    # 나의 점수가 몇번 인덱스에 있는지 확인
    for i in avg:
        answer.append(avgsort.index(i)+1)

    return answer
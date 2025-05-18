'''
처음 시도: 
배열을 오름차순으로 정렬한 뒤에, 먼저 citations 내에서 조건을 만족하는지 확인하고
조건을 만족하는 수가 없으면 citations[0]보다 작은 수를 확인
'''
def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] < i+1:
            return i
        
    return len(citations)
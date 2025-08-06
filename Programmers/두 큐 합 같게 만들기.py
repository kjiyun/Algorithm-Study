# while 문 안에서 sum을 반복해서 시간초과 발생 
# -> sum은 미리 계산해두고 뺀 값과 더한 값만 계산하는 방식 적용
from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    if (sum(queue1) + sum(queue2)) % 2 != 0: # 합이 홀수라 두 큐의 합이 같을 수 없음
        return -1
    
    cnt = 0
    while True:
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            cnt += 1
        elif sum1 < sum2:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
            cnt += 1
        else:
            return cnt
        
        if cnt > 2*len(queue1) + 2*len(queue2):
            return -1
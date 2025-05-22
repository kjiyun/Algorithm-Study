'''
deque와 enumerate를 잘 활용해야 하는 문제

'''

from collections import deque

def solution(priorities, location):
    answer = 0
    result = []
    
    priorities = enumerate(priorities)
    priorities = deque(priorities)
    
    while len(priorities) > 0:
        max_i = 0
        pi, pnum = priorities[0]
        for i in range(1, len(priorities)):
            ti, tnum = priorities[i]
            if pnum < tnum: # 우선순위가 더 높은 것이 있는 경우
                pnum = tnum
                max_i = i
        # print("pn", max_i, pnum)
        for _ in range(max_i):
            priorities.append(priorities.popleft())
        result.append(priorities.popleft())
        # print("priori", priorities)
    
    for k in range(len(result)):
        if result[k][0] == location:
            answer = k+1
        
    return answer
'''
처음 시도한 방식은
다리 안에 들어갈 수 있는 리스트를 구해놓고,
다리 안에 트럭이 1개인 경우 -> bridge_length 만큼 더하기
다리 안에 트럭이 2개 이상인 경우 -> bridge_length + (개수-1) 만큼 더하기
마지막에 +1 수행
=> 하지만 실패 ㅠ

**
pop(0) ➡ popleft() 로 바꿔라
collections 라이브러리의 dequeue을 사용하자

List.pop(0)의 시간복잡도 : O(N)
dequeue.popleft()의 시간복잡도 : O(1)
'''

from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    bridge = deque([0] * bridge_length) # 다리 위에 있는 트럭 정보
    truck_weights = deque(truck_weights)
    current_weight = 0
    
    while len(truck_weights) > 0:
        time += 1
        current_weight -= bridge[0]
        bridge.popleft()
        
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
    
    time += bridge_length
    
    return time


def solution(bridge_length, weight, truck_weights):
    answer = 0
    result = []
    cnt = 0
    total_weight = 0
    idx = 0
    
    while idx < len(truck_weights):
        if total_weight + truck_weights[idx] <= weight:
            total_weight += truck_weights[idx]
            # print("test", total_weight, idx)
            cnt += 1
            idx += 1
        else:
            # print("hello")
            result.append(cnt)
            cnt = 0
            total_weight = 0
    if total_weight != 0:
        result.append(cnt)
    # print(result)
    for r in result:
        if r == 1:
            answer += bridge_length
        else:
            answer += (bridge_length + r - 1)
    answer += 1
    
    return answer
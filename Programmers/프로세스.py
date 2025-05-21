from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque((i, j) for i, j in enumerate(priorities))
    print("queue", queue)
    
    while queue:
        process = queue.popleft()
        if queue and any(process[1] < q[1] for q in queue):
            queue.append(process)
            print("pri:",priorities)
        else:
            answer += 1
            print(process)
            if process[0] == location:
                return answer

    # return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))
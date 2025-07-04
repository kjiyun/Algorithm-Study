'''
하나의 숫자가 +n, *2, *3 중 하나씩 반복해서 수행하면서 최소 수행 횟수를 찾는 문제
-> 처음에는 최소이므로 greedy 문제 또는 dfs라고 생각함
-> 시간 초과 발생

x -> x+n, x*2, x*3 으로 한 칸씩 이동하며 y에 도달할 수 있는 최소 횟수를 찾기
즉, 최단거리(BFS) 문제 !
'''
from collections import deque

def solution(x, y, n):
    answer = 0

    visited = set()
    queue = deque()
    queue.append((x, 0)) # 현재 값과 수행 횟수

    while queue:
        cur, cnt = queue.popleft()

        if cur == y:
            return cnt

        for nxt in (cur+n, cur*2, cur*3):
            if nxt <= y and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, cnt+1))
    return -1


print(solution(10, 40, 5))
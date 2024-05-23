# 최대 합

#시간초과
import sys

n = int(sys.stdin.readline())
q = [0]*n

for _ in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        q.append(a)
    else:
        print(max(q))
        q.remove(max(q))

# 다른 방법
import sys
import heapq
# heappop(), heappush() 함수는 최소힙만 동작하기 때문에 최대힙을 구현하기 위해서는 변형필요.

n = int(sys.stdin.readline())
q = []

for _ in range(n):
    a = int(sys.stdin.readline()) * -1  # -1을 곱해서 가장 큰 값이 음수가 되면 가장 작은 값이 되도록한다.
    if a != 0:
        heapq.heappush(q, a) # q에 a를 push 한다.
    else:
        try:
            print(-1 * heapq.heappop(q)) # q에서 가장 작은 값을 pop한다.
        except:
            print(0) # q에 값이 없다면 0을 출력한다.
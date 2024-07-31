# 카드2
from collections import deque

card = deque()
n = int(input())

for i in range(n):
    card.append(i+1)

while len(card) > 1:
    card.popleft()  #가장 먼저 추가된 요소가 제거됨
    card.append(card.popleft())

print(card[0])

#Queue() 클래스를 사용한 방법 -> 틀림
import queue

card = queue.Queue()
n = int(input())

for i in range(n):
    card.put(i+1)

while card.qsize() > 1:
    card.get()
    card.put(card.get())

print(card.queue) # 요소가 아닌 deque([4]) 형태로 출력됨
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
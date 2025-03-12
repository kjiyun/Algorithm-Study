#30804
# 양 쪽 끝을 제거할 수 있다는 말은 슬라이딩 윈도우로 묶어서 계산할 수 있다는 의미
# set은 시간 복잡도 높으므로 defaultdict 사용


import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

max_len = 0
count_fruit = defaultdict(int) # 과일 종류 수 정보를 가지는 dict
fruit_type = 0 #과일 종류 수
current_list = deque() # 현재 꼬치에 있는 과일

for i in range(n):
    current_list.append(s[i])
    count_fruit[s[i]] += 1

    if count_fruit[s[i]] == 1:
        fruit_type += 1

    while fruit_type >= 3: #과일이 3종류 이상인 경우
        remove_fruit = current_list.popleft()
        count_fruit[remove_fruit] -= 1

        if count_fruit[remove_fruit] == 0:    
            fruit_type -= 1

    max_len = max(max_len, len(current_list))

print(max_len)

#지능형 기차 2
cnt = 0
max_cnt = 0

for _ in range(10):
    o, i = map(int, input().split())
    cnt -= o
    cnt += i
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)
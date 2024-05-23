# 연속합

# 음수의 인덱스를 먼저 알아내고 나머지 부분의 합을 구하기

#시간 초과 문제 발생
n = int(input())
p = list(map(int, input().split()))

sum_list = [0] * n
start = 0
finish = n-1
for i in range(n):
    if max(p) >= 0 and (p[i] < 0 or i == finish):  #음수가 나오거나 인덱스가 마지막인 경우
        sum = 0
        for j in range(start, i):
            sum += p[j]
        sum_list.append(sum)
        start = i+1
    if max(p) < 0: #리스트 원소가 모두 음수인 경우
        sum_list.append(max(p))
        sum_list.remove(0)
print(max(sum_list))

# 다른 방법
n = int(input())
p = list(map(int, input().split()))

for i in range(1, n):
    p[i] = max(p[i], p[i-1]+p[i])

print(max(p))
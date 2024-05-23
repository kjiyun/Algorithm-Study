# ATM

n = int(input())  # 사람 수
p = list(map(int, input().split()))  # 각 사람이 돈을 인출하는 데 걸리는 시간

p = sorted(p)

sum = 0
for i in range(n):
    for j in range(i+1):
        sum += p[j]

# 아래의 방식으로도 해결가능
# for i in range(1, n+1):
#     answer += sum(p[0:i])

print(sum)
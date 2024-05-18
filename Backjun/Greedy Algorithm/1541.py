# 잃어버린 괄호

exp = input().split('-') #'-'를 기준으로 분리하기
print(exp)

num = [] # '-'로 나눈 각 항들의 합을 저장하는 리스트

for i in exp:
    sum = 0
    tmp = i.split('+') # 수를 알기 위해 + 기준으로 분리
    for j in tmp:
        sum += int(j)
    num.append(sum)

n = num[0]

for i in range(1, len(num)):
    n -= num[i]
print(n)
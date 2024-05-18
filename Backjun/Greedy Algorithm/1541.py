# 잃어버린 괄호

exp = input().split('-') #'-'를 기준으로 분리하여 리스트에 저장

num = [] # '-'로 나눈 각 항들의 합을 저장하는 리스트

for i in exp:
    sum = 0
    tmp = i.split('+') # 수를 알기 위해 + 기준으로 분리
    for j in tmp: 
        sum += int(j)  # 각 수를 더하기
    num.append(sum)  # 더한 결과값을 num에 저장

n = num[0] #항들의 합의 첫번째 원소를 n에 저장

for i in range(1, len(num)):
    n -= num[i] 
print(n)
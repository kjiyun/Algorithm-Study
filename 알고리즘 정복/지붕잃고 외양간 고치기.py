'''
전체 큰 흐름에 대해 주석 먼저 달기!

필요한 자료들을 어떻게 활용하는지가 중요했던 문제

'''

answer = 0
# 판자수, 외양간수, 소의 수 입력
m, s, c = map(int, input().split())
cows = []

for _ in range(c):
    cows.append(int(input()))

dist = []
cows.sort()
for i in range(1, c):
    temp = cows[i] - cows[i-1] - 1
    dist.append(temp) # 0도 들어가 있음
    
dist.sort(reverse=True)

# 1개 짜리 가장 큰 판자 크기(맨 뒤 소 - 맨 앞 소 + 1)
answer = cows[-1] - cows[0] + 1

# m개인 경우 가장 큰 값부터 빼줌
for i in range(m-1):
    answer -= dist[i] # 가장 큰 차이를 빼는 것

# 결과 출력
print(answer)
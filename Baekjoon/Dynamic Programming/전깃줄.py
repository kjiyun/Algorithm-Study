'''
전깃줄이 교차하지 않으려면 input이 커질수록 output도 커져야함
=> 가장 긴 증가하는 부분 수열을 찾는 문제와 매우 유사
A를 배열의 index로 취급하므로 순서대로 정렬 필요 -> elec.sort(key=lambda x:x[0])
'''

import sys
input = sys.stdin.readline

n = int(input())
elec = []
for _ in range(n):
    elec.append(list(map(int, input().split())))
elec.sort(key=lambda x:x[0]) # 전봇대 A를 index로 둬야 하므로 A를 기준으로 정렬
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if elec[i][1] > elec[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))
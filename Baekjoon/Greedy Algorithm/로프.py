# 모든 로프를 사용할 필요가 없으므로 먼저 오름차순 sort후에 각각 비교해보는 방식
import sys
input = sys.stdin.readline

n = int(input())
weights = []
for _ in range(n):
    weights.append(int(input()))

max_weight = -1e9
weights.sort(reverse=True)
for i in range(n):
    w = weights[i]*(i+1)
    max_weight = max(w, max_weight)
print(max_weight)
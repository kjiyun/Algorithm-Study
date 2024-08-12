#블랙잭

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] > m:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)

#다른 방법: combinations 함수 사용
from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for cards in combinations(arr, 3):  
    if sum(cards) <= m:
        result = max(result, sum(cards))
print(result)
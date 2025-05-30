import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [] # 동전의 가치
for _ in range(n):
    a.append(int(input()))

result = 0
a.sort(reverse=True)
for i in range(n):
    if k // a[i] > 0: # 나누어떨어지는 경우 멈춤
        result += k // a[i]
        k = k % a[i]
    
    if k == 0:
        break
print(result)
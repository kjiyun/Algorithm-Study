#약수 구하기

n, k = map(int, input().split())
rem = []

for i in range(1, n+1):
    if n % i == 0:
        rem.append(i)

if len(rem) >= k:
    print(rem[k-1])
else:
    print(0)
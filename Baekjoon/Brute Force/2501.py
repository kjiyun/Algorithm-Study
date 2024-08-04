#약수 구하기

n, k = map(int, input().split())
div = []

for i in range(n):
    if n % (i+1) == 0:  # i+1로 나누어진다면
        div.append(i+1)

if len(div) >= k:  #n의 약수의 개수가 k개보다 많은 경우 + 같은 경우!!
    print(div[k-1])
else:
    print(0)
import sys
input = sys.stdin.readline

n = int(input())
plans = [[0,0]]
price = [0]*(n+2)

for _ in range(n):
    t, p = map(int, input().split())
    plans.append((t, p))

for i in range(1, len(plans)):
    if i + plans[i][0] <= n+1:
        for k in range(i + plans[i][0], n+2):
            if price[k] < price[i] + plans[i][1]:
                price[k] = price[i] + plans[i][1]
print("price", price)
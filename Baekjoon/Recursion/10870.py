# 피보나치 수 5

n = int(input())
f = [0]*(n+1)


for i in range(n+1):
    if i == 0:
        f[i] = 0
    elif i == 1:
        f[i] = 1
    else:
        f[i] = f[i-1] + f[i-2]

print(f[n])
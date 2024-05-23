# 포도주 시식

n = int(input())
arr = [0] * (n+1)
sum = [0] * (n+1)

for i in range(1, n+1):
    arr[i] = int(input())

if (n < 2):
    print(arr[n])
else:
    sum[1] = arr[1]
    sum[2] = arr[1] + arr[2]

    for i in range(3, n+1):
        # 현재 포도주를 마시지 않는 경우도 고려해야 한다.
        sum[i] = max(sum[i-1], sum[i-3]+arr[i-1]+arr[i], sum[i-2]+arr[i])

    print(sum[n])

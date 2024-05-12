# 계단 오르기

n = int(input())
stair = [0] * (n+1) #각 계단에서의 점수
arr = [0] * (n+1) #최댓값 입력

for i in range(1, n+1):
    stair[i] = int(input())

if n < 2: #주어진 계단 수가 2보다 적은 경우를 처리하지 않으면 런타임 에러 발생
    print(stair[n])
else:
    arr[1] = stair[1]
    arr[2] = arr[1] + stair[2]

    for j in range(3, n+1):
        arr[j] = max(arr[j-3] + stair[j-1], arr[j-2]) + stair[j]

    print(arr[n])
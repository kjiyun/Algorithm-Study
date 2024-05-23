# 숫자의 합

n = int(input())
arr = list(map(int, input()))
sum = 0

for i in range(n):
    sum += arr[i]

#print(sum(arr))로도 한방에 가능
print(sum)
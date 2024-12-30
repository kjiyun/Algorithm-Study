# 진법 변환 2

n, b = map(int, input().split()) # 10진법 수
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while n:  #몫이 0이 될 때까지 반복
    s += str(arr[n%b]) # 나머지를 추가
    n //= b  #몫을 갱신

print(s[::-1])
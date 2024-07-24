#세탁소 사장 동혁

t = int(input())  #테스트 케이스의 개수

for _ in range(t):
    c = int(input())  #거스름돈
    q = c // 25
    d = (c - q*25) // 10
    n = (c - q*25 - d*10) // 5
    p = c - q*25 - d*10 - n*5
    print(q, d, n, p)

# 조금 더 간단한 방법
n = int(input())

for _ in range(n):
    money = int(input())
    for i in [25, 10, 5, 1]:
        print(money//i, end='')  # 몫 출력
        money = money%i  # 나머지 값 저장
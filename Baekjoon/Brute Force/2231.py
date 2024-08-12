#분해합

n = int(input())
result = 0

for i in range(n):
    #각 숫자의 자리수 합과 숫자 자신의 합
    digit_sum = i + sum(map(int, str(i)))
    #생성자인지 검사
    if digit_sum == n:
        print(i)
        break
else:
    print(0)
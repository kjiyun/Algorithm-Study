#이진수

t = int(input()) #테스트 케이스의 개수

for i in range(t):
    n = int(input())
    result = []
    cnt = 0

    #십진수를 이진수로 변환하는 방법
    while n > 0:
        if n % 2 == 1:
            print(i, end=' ')
        n = n // 2
        cnt += 1

#내장함수 사용 방법
for _ in range(int(input())):
    n = bin(int(input()))[2:]  #bin()은 10진수를 2진수로 바꿈, 0b1101 형식으로 오기때문에 0b를 제외하도록 [2:]추가
    for i in range(len(n)):
        if n[-i-1] == '1': #2진수의 값의 역순을 봐야하므로
            print(i, end=' ')
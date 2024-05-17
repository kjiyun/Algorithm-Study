# 동전 0

n, k = map(int, input().split())

# 가지고 있는 동전의 종류를 리스트의 형태로 입력받는다.
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)  # 역순으로 변경

answer = 0
for coin in coins:
    if k >= coin:
        answer += k // coin  # k값을 coin으로 나눈 몫을 저장한다.
        k %= coin  # 나머지는 k에 업데이트
        if k <= 0:  # 나머지가 없다면 끝내기
            break

print(answer)        
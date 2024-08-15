#영화감독 숌

#브루트 포스는 가능한 모든 수를 조합하는 방식이다. 따라서 숫자를 셀 카운트 변수와 초기값 666을 설정한 결과값 변수를 선언한 뒤 반복문을 사용한다.
n = int(input())
cnt = 0
result = 666

while True:
    if '666' in str(result):
        cnt += 1
    if cnt == n:
        break
    result += 1 # result 값을 1씩 증가시켜 cnt의 수가 n이 될 때까지 반복한 뒤 while문을 빠져나오도록 한다.
print(result)
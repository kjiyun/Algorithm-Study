# 그대로 출력하기

while True:
    try:
        print(input()) 
    except EOFError:
        break

# sys.stdin.readline()으로 입력받으면 오류 발생
# input()은 EOF를 받을 때 EOFError를 일으키지만 sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴하기 때문이다.
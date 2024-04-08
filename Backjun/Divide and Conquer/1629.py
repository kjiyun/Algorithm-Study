# 곱셈**

a, b, c = map(int, input().split())
result = 1

for i in range(b):
    result *= a

print(result % c)  # 시간 초과

# 다른 방법
# 참고 : https://velog.io/@grace0st/%EA%B3%B1%EC%85%88-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
"""
    지수 법칙: A^m+n = A^m x A^n
    나머지 분배 법칙: (AxB)%C = (A%C) *(B%C) % C

    2^32라면 2를 32번 곱하는 방법도 있지만, 
    (2^16)^2로 해서 풀면 2를 16번 곱한 것을 다시 2번 곱하니 
    17번의 연산만으로 끝낼 수 있어서 시간이 훨씬 적게 든다.
"""
import sys
a,b,c = map(int, sys.stdin.readline().split())

def multi(a,b):
    if b == 1:
        return a%c
    else:
        tmp = multi(a, b//2)
        if b%2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(multi(a,b))
# 이항 계수 3 ******* 중요 *******

# 방법1: 재귀함수 이용
# n, k = map(int, input().split())

# def bin(n, k):
#     if ((k==0) or (k==n)):
#         return 1
#     else:
#         return (bin(n-1, k-1) + bin(n-1, k))
    
# print(bin(n, k)%1000000007)
# 위의 방법은 n의 제한이 매우 크기 때문에 O(N^2)의 알고리즘으로는 시간초과가 걸린다.

# 방법2: dynamic programming 이용
# n, k = map(int, input().split())

# arr = [[0]*100]*100
# def bin(n, k):
#     for i in range(0, n+1):
#         print('oo:',i)
#         for j in range(0, min(i, k)+1):
#             if ((j==0) or (j==i)):
#                 arr[i][j] = 1
#                 print('1 :', arr[i][j])
#             else:
#                 arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
#                 print('arr', arr[i][j])
#     print('arr[1][2]', arr[2][1], arr[2][2])
#     return arr[n][k]

# print(bin(n, k)%1000000007)

# 방법3: 페르마의 소정리 이용
# 페르마의 소정리 : p가 소수이고 a가 p의 배수가 아니면 a^(p-1) = 1 (mod p) 이 성립한다.
# 참고 : https://abcdefgh123123.tistory.com/350

# n, k = map(int, input().split())
# P = 1000000007

# def factorial(num):
#     result = 1
#     for i in range(2, num+1):
#         result = (result * i) % P
#     return result

# # 거듭제곱 계산
# def square(num, k):
#     if k == 0:
#         return 1
#     elif k == 1:
#         return num
    
#     tmp = square(num, k//2)
#     if k % 2:
#         return (tmp * tmp * n) % P
#     else:
#         return (tmp * tmp) % P
    
# top = factorial(n)
# bot = factorial(k) * factorial(n-k)
# print(bot)
# print(top * square(bot, P-2) % P)


# 참고 : https://sweetburble.tistory.com/153
# 팩토리얼 값 계산 (나머지 연산 적용)
def factorial_with_rest(N, rest):
    n = 1
    for i in range(2, N+1):
        n = (n * i) % rest
    return n

# 거듭제곱 계산 (나머지 연산 적용)
def reduce_pow(a, b, c):
    if (b == 1):
        return a % c

    X = reduce_pow(a, b//2, c)

    if (b % 2 == 0): # 짝수라면
        return X * X % c
    else: # 홀수라면
        return a * X * X % c


N, K = map(int, input().split())
P = 1000000007

first = factorial_with_rest(N, P)
second = factorial_with_rest(K, P) * factorial_with_rest(N-K, P)

print(first * reduce_pow(second, P-2, P) % P)
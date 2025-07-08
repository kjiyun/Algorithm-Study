def solution(n, k):
    answer = []
    n_list = [i for i in range(n+1)]

    # 전체 가능한 경우의 수 구하기
    total = 1
    for i in range(2, n+1):
        total *= i

    # n! // (n-1)! => 몫: 첫 수 나옴
    while len(n_list) > 2:
        if k % (total // n) == 0:
            target = k // (total // n)
            answer.append(n_list[target])
            del n_list[target]
        else:
            target = k // (total // n) + 1
            answer.append(n_list[target])
            del n_list[target]
        total = total // n  # (n-1)!
        n -= 1
        # k 업데이트
        if k < total:
            continue
        elif k >= total and k % total == 0:
            k = total
        else:
            k = k % total

    answer.append(n_list[-1])

    return answer

### 다른 사람 풀이
from collections import deque

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def solution(n, k):
    answer = []
    deq = deque([i for i in range(1, n+1)])

    while n > 1:
        fac = factorial(n-1)
        num = deq[(k-1)//fac]
        answer.append(num)
        deq.remove(num)
        n -= 1
        k %= fac

    answer.append(deq[-1])
    return answer
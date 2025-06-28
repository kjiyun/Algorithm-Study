'''
주의할 점:
    동일한 길이인 경우 높은 것만 남긴다.
    순서는 상관없음

풀이 방식:
    1. 조합으로 모든 경우를 만들어 보기
    2. 해당 경우는 dict 형태로 같은 문자가 있으면 +1
    3. 2번 이상 반복되는 코스는 opt_order에 저장 후 최대 횟수인지 체크
    4. 최대 횟수로 업데이트
'''
from itertools import combinations

def solution(orders, course):
    answer = []

    for c in course:
        order = dict()
        for o in orders:
            for k in combinations(o, c):
                k = list(k)
                k.sort()
                k = ''.join(k)

                if k not in order:
                    order[k] = 1
                else:
                    order[k] += 1
        
        max_num = -1e9
        opt_order = []
        for o, n in order.items():
            if n >= 2:
                if max_num == n:
                    opt_order.append(o)
                elif max_num < n:
                    max_num = n
                    opt_order = []
                    opt_order.append(o)

        for i in opt_order:
            answer.append(i)
    answer.sort()

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
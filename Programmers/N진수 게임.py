# 시간 초과를 해결해야하는 문제

# 2진수 구하는 코드
def to_base_n(num, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(num, base)  # q:몫, r:나머지
    
    if q == 0:
        return arr[r]
    else:
        return to_base_n(q, base) + arr[r]

def solution(n, t, m, p):
    answer = ''
    
    # t*m 만큼 후보를 두고 거기서 가져오는 걸로 하기
    num = 0
    total = ''
    while len(total) < t*m:
        total += str(to_base_n(num, n))
        num += 1
    
    while len(answer) < t:
        answer += total[p-1]
        p += m
    
    return answer
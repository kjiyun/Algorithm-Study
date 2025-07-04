def solution(numbers):
    answer = []
    
    for num in numbers:
        b = '0'
        if num == 1:
            answer.append(2)
            continue
        
        if num % 2 == 0: # 짝수인 경우: +1만 하면됨 0으로 끝나므로
            answer.append(num+1)
        else: # 홀수인 경우: 01 -> 10 로 변경
            b += bin(num)[2:]
            idx = b.rfind('01')
            b = list(b)
            b[idx], b[idx+1] = '1', '0'
            answer.append(int(''.join(b), 2))
                
    return answer
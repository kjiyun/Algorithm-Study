def solution(n, arr):
    answer = 0
    ps = [0]
    
    # 누적합이 음수가 되면 reset
    for i in range(n):
        if ps[-1] + arr[i] < 0:
            ps.append(0)
        else:
            ps.append(ps[-1] + arr[i])
    answer = max(ps)
    return answer
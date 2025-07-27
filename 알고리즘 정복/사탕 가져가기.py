def solution(n, k, arr):
    answer = 0
    prefix_sum = []
    
    if n < k:
        return sum(arr)
    else:
        prefix_sum.append(sum(arr[:k]))
    
    # 미리 해당 위치부터 k개까지의 합을 구해두기
    for i in range(1, n-k+1):
        prefix_sum.append(prefix_sum[-1]+arr[i+k-1]-arr[i-1])
    answer = max(prefix_sum)
    
    return answer

def solution(n, k, arr):
    answer = 0
    prefix_sum = [0]

    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + arr[i])

    for i in range(k, n+1):
        temp = prefix_sum[i] - prefix_sum[i-k]
        answer = max(temp, answer)

    return answer
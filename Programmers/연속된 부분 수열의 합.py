"""
    sequence에서 연속된 수들의 합이 k가 되는 구간 중 가장 짧은 구간의 인덱스 구하기
    연속된 부분합 + 가장 짧은 길이 => 슬라이딩 윈도우, 투 포인터 적합

    연속된 구간을 구하는가, 구간의 합을 구하는가, 조건을 만족하는 가장 짧은/긴 구간을 찾는가 체크
"""

def solution(sequence, k):
    start, end = 0, 0
    current_sum = 0
    best_length = int(1e9)

    while end < len(sequence):
        current_sum += sequence[end]
        while current_sum >= k and start <= end:
            if current_sum == k:
                if end - start + 1 < best_length:
                    best_length = end - start + 1
                    answer = [start, end]
            current_sum -= sequence[start]
            # 합이 k 이상되면 start을 뒤로 하면서 최소 길이를 갱신
            start += 1
        end += 1
    
    return answer
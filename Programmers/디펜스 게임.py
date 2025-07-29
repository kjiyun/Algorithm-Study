import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    
    # 남은 병사의 수 < 현재 라운드의 적의 수 => 게임 종료
    # 무적권은 k번
    
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])
        n -= enemy[i]
        if n < 0:
            if k == 0:
                return i
            max_num = -heapq.heappop(heap)
            n += max_num
            k -= 1
    return len(enemy)
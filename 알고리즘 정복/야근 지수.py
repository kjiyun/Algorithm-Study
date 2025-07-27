import heapq

def solution(n, works):
    answer = 0
    
    heap = []
    """오름차순으로 정렬하려면 음수로 변경해서 정렬!!"""
    for w in works:
        heapq.heappush(heap, -w)
    # heap = [-4, -3, -3]
    
    if sum(works) <= n: # 남은 작업량이 없을 경우
        return 0
    
    for _ in range(n):
        while heap[0] >= 0:
            heapq.heappop(heap)           
        heapq.heappush(heap, heapq.heappop(heap) + 1)
        
    for h in heap:
        answer += h**2
    
    return answer
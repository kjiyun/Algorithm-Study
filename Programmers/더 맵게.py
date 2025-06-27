import heapq

def solution(scoville, K):
    answer = 0

    heap = []
    for s in scoville:
        heapq.heappush(heap, s) #이렇게 하면 저절로 작은순서대로 배열됨

    while heap[0] < K: #스코빌 지수보다 낮은 음식이 있는 경우
        if len(heap) == 1: #K 이상으로 만들 수 없음
            return -1
        food1 = heapq.heappop(heap) #가장 앞에있는 것 나옴
        food2 = heapq.heappop(heap)
        tmp = food1 + food2 * 2
        heapq.heappush(heap, tmp)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
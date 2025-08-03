import heapq

def solution(jobs):
    answer = 0
    heap = [] # 대기 큐
    
    # (소요시간, 요청시각, 번호) 형태로 heap에 넣기
    # 소요시간이 짧은 순서, 소요시간이 같다면 요청시각이 빠른 순서
    jobs.sort(key=lambda x:(x[0], x[1]))
    now, i, total_time = 0, 0, 0

    while i < len(jobs) or heap:
        while i < len(jobs) and jobs[i][0] <= now:
            request, duration = jobs[i] # 요청시각, 소요시간
            heapq.heappush(heap, (duration, request, i))
            i += 1
        
        if heap:
            duration, request, idx = heapq.heappop(heap)
            now += duration
            total_time += now - request
        else:
            now = jobs[i][0]
    
    return total_time // len(jobs)
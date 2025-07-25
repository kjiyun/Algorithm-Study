from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    for c in cities:
        c = c.upper()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            answer += 1
        else:
            if cacheSize > 0 and len(cache) >= cacheSize:
                cache.popleft()
            if cacheSize > 0:
                cache.append(c)
            answer += 5
    
    return answer
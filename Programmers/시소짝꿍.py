from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)

    for w, n in counter.items():
        if n >= 2:
            answer += (n*(n-1)/2)
    
    weights = set(weights) # 중복 제거

    for w in weights:
        if w * 2/3 in weights:
            answer += counter[w*2/3] * counter[w]
        if w * 3/4 in weights:
            answer += counter[w*3/4] * counter[w]
        if w * 1/2 in weights:
            answer += counter[w*1/2] * counter[w]
                
    return answer

print(solution([100,180,360,100,270]))
def solution(clothes):

    hash_map = {}
    answer = 0

    for cloth in clothes:
        if cloth[1] in hash_map:
            hash_map[cloth[1]] += 1
        else:
            hash_map[cloth[1]] = 1
    
    answer = 1
    for i in hash_map.values():
        answer *= (i+1)

    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
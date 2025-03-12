def solution(genres, plays):
    answer = []
    dict1 = {} # genre와 play 매핑 딕셔너리
    dict2 = {} # 장르별 전체 재생 횟수 기록 딕셔너리

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dict1:
            dict1[g] = [(i, p)]
        else:
            dict1[g].append((i, p))

        if g not in dict2:
            dict2[g] = p
        else:
            dict2[g] += p
    print(dict1, dict2)

    for (k, v) in sorted(dict2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dict1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))

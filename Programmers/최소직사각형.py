def solution(sizes):
    w = []  # 각 행별로 비교해서 큰 값을 넣기
    h = []

    for size in sizes:
        if size[0] > size[1]:
            w.append(size[0])
            h.append(size[1])
        else:
            w.append(size[1])
            h.append(size[0])
        

    answer = max(w) * max(h)
    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))
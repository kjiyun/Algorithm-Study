import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]

    for _ in range(n-1):
        a, b = map(int, input().split())
        graph[b].append(a)  # a가 b의 부모
    
    p, q = map(int, input().split())  # 가장 가까운 공통 조상을 구할 두 노드

    p_list = []
    q_list = []

    # 부모로 이동하면서 리스트에 저장
    for num in [p,q]:
        i = num
        arr = [num]
        while True:
            if graph[i] == []:
                break
            for k in graph[i]:
                arr.append(k)
                i = k
        if num == p:
            p_list = arr
        else:
            q_list = arr

    p_list.reverse()
    q_list.reverse()

    min_len = min(len(p_list), len(q_list))

    for i in range(min_len):
        if p_list[i] != q_list[i]:  # 값이 다른 경우 공통 조상을 벗어난 것
            print(p_list[i-1])  # 직전의 값이 가장 가까운 공통 조상이 됨
            break
    else: # 하나가 다른 것의 조상인 경우 -> for문 전체에 대한 else
        print(p_list[min_len - 1])
#요세푸스 문제0

#시간복잡도: O(N)
n, k = map(int, input().split())
idx = 0
queue = ([i+1 for i in range(n)])
res = []

while queue: #요소가 모두 제거될 때까지 진행
    idx += k-1
    if idx >= len(queue):
        idx = idx % len(queue) #index 계산
    res.append(str(queue.pop(idx)))    

print("<", ", ".join(res), ">", sep="")

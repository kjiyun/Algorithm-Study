from collections import deque

def solution(begin, target, words):

    def bfs(word, n):
        queue = deque()
        queue.append((word, n))
        # print('queue', queue)
        
        while queue:
            p, q = queue.popleft()
            # print("pq", p, q)

            if p == target:
                break
            
            for w in words:
                count = 0
                for i in range(len(w)):
                    if w[i] == p[i]:
                        count += 1
                    if count == len(w)-1:
                        queue.append((w, q+1))
        print("n", q)
        return q # 변환 횟수 전달
    
    if target not in words:
        return 0
    bfs(begin, 0)
    # print(answer)
    # return answer # 시작 단어와 변환 횟수 전달

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin, target, words)
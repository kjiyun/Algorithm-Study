from collections import deque

def solution(begin, target, words):

    def bfs(word):
        queue = deque()
        queue.append([word, 0])

        while queue: 
            r, cnt = queue.popleft()
            
            if r == target:
                return cnt
            
            for w in words:
                count = 0
                for i in range(len(w)): # ex) 'hot'
                    if r[i] == w[i]:
                        count += 1
                    if count == len(w)-1: #알파벳 하나만 다른 경우
                        queue.append([w, cnt+1])
        return cnt

    if target not in words:
        return 0
    
    else:
        return bfs(begin)
        

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin, target, words)
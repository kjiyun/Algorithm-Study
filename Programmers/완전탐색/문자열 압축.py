'''
**완전탐색 문제**

자르는 문자열 단위를 1부터 2/n까지 반복한다.
여기서 중요한 점은 단위를 정하고 나서 첫 구간은 tmp에 미리 저장해둔다.
그리고 그 다음 구간과 비교한다. 다음 구간과 비교가 끝나면 그때 tmp를 해당 구간으로 변경한다.
'''

def solution(s):
    result = []

    if len(s) == 1:
        return 1

    for c in range(1, len(s)//2+1):
        sentence = ''
        cnt = 1
        tmp = s[:c]
        for i in range(c, len(s)+c, c):
            if tmp == s[i:i+c]:
                cnt += 1
            else:
                if cnt > 1: # 반복되는 구간이 중단된 경우
                    sentence = sentence + str(cnt) + tmp
                else:
                    sentence = sentence + tmp
                cnt = 1
                tmp = s[i:i+c]
    
        result.append(len(sentence))

    return min(result)

print(solution("aabbaccc"))
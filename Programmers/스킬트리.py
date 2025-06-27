'''
skill_trees의 길이가 1이상 20이하이고, skill의 길이는 1이상 26이하이므로 
완전탐색을 수행하면 약 26**20일 것 같은데
완전탐색을 하는 문제인지 여부가 헷갈림

1. tree에서 skill에 포함된 문자만 추출
2. 그 추출된 순서가 skill의 prefix인지 확인
'''

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        tmp = ''
        for t in tree:
            if t in skill:
                tmp += t
    
        if tmp == skill[:len(tmp)]:
            answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
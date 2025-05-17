'''
header가 없으므로 열의 번호를 list로 만들어서 리스트를 순열로 만듦
먼저 튜플로 유일성을 판단한 뒤에 issubset으로 최소성 판단
Today I Learn: 
"tuple(relation[row][key] for key in keys)" : set은 순서 상관없음, tuple은 순서 상관있으며 수정 불가능
"set(i).issubset(set(j))" : 부분집합 확인용
combinations에는 (리스트, 정수) 순서로 들어갈 수 있음
'''

from itertools import combinations

def solution(relation):
    idx_list = []
    result = []

    for idx, _ in enumerate(relation[0]):
        idx_list.append(idx)

    for i in range(len(relation[0])):
        for keys in combinations(idx_list, i+1):
            tuple_list = set()
            # 튜플로 유일성 확인
            for row in range(len(relation)):
                v = tuple(relation[row][key] for key in keys) # set은 순서를 보장하지 않으므로 (1, 2)과 (2, 1)을 동일하게 생각할 수 있으므로 tuple로 변경해야함
                tuple_list.add(v)

            if len(relation) == len(tuple_list):
                result.append(keys) # 유일성 만족하는 set 저장

    # 최소성 여부 확인
    remove_set = set()
    for i in result: # 검사하는 항목
        for j in result:
            if i == j:
                continue
            if set(i).issubset(set(j)):
                remove_set.add(j)
    answer = []
    for x in result:
        if x not in remove_set:
            answer.append(x)
    
    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
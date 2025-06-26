'''
내가 생각한 방식:
문자열을 파싱해서 집합 리스트로 만들기
'''

def solution(s):
    answer = []
    s_list = []

    # s를 리스트로 변환
    flag = False
    for i in range(1, len(s)-1):
        if s[i] == '{':
            flag = True
            tmp = []
            tmp_num = ''
            continue
        elif s[i] == '}':
            tmp.append(int(tmp_num))
            flag = False
            s_list.append(tmp)
            tmp = []
        
        if flag:
            if s[i] == ',':
                tmp.append(int(tmp_num))
                tmp_num = ''
            else:
                tmp_num += s[i]

    # 길이순 정렬
    s_list.sort(key=len)

    # 순서 복원
    for sl in s_list:
        for i in sl:
            if i not in answer:
                answer.append(i)

    return answer

print("1:", solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print("2:", solution('{{20,111},{111}}'))
def solution(str1, str2):
    answer = 0
    list1 = []
    list2 = []

    # 두개씩 끊어보기
    for i in range(0, len(str1)-1):
        # 영문자로 된 글자 쌍만 유효
        if str1[i:i+2].isalpha():
            tmp = str1[i:i+2].upper()
            list1.append(tmp)
        
    for i in range(0, len(str2)-1):
        if str2[i:i+2].isalpha():
            tmp = str2[i:i+2].upper()
            list2.append(tmp)
        

    # 다중합집합
    tmp1 = list1.copy()
    result1 = list1.copy()

    for i in list2:
        if i not in tmp1:
            result1.append(i)
        else:
            tmp1.remove(i)

    # 교집합
    result2 = []

    for i in list2:
        if i in list1:
            list1.remove(i)
            result2.append(i)

    if len(result1) == 0 and len(result2) == 0:
        answer = 1 * 65536
    else:
        answer = int(len(result2)/len(result1) * 65536)
    return answer

print(solution("FRANCE", "french"))
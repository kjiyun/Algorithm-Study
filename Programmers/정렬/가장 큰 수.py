# 0으로 시작하는 정수 주의

def solution(numbers):
    answer = ''
    max_num = 0
    idx = 0
    
    #가능한 조합을 리스트로 만들기
    while len(numbers) > 0:
        for i in range(len(numbers)):
            if max_num < int(str(numbers[i])[0]):
                # print("num", numbers[i])
                max_num = int(str(numbers[i])[0])
                idx = i
            if max_num == int(str(numbers[i])[0]) and numbers[i] > 9 and numbers[idx] > 9: # 둘다 두 자리 이상의 수일 때
                if numbers[i] > numbers[idx]:
                    idx = i
            elif max_num == int(str(numbers[i])[0]) and numbers[i] > 9:
                if int(str(numbers[i])[1]) > int(str(numbers[i])[0]):
                    idx = i
                
        answer += str(numbers[idx])
        del numbers[idx]
        # print(answer)
        max_num = 0

    if len(answer) > 0 and answer[0] == '0':
        answer = 0
    return answer

print(solution([]))
def solution(fees, records):
    answer = dict()
    result = []
    inside = dict()
    money = 0

    # records 정리
    for record in records:
        time, num, status = record.split()
        if status == "IN":
            h, m = map(int, time.split(":")) # 시간 계산
            inside[num] = h * 60 + m
        elif status == "OUT":
            h, m = map(int, time.split(":")) # 시간 계산
            spent = h*60 + m - inside[num] # 이용한 시간

            if num not in answer:
                answer[num] = spent
            else:
                answer[num] += spent

            del(inside[num])

    # 아직 안나간 차량이 있는 경우 (23:59에 출차된 것으로 간주)
    for n, s in inside.items():
        spent = 23*60 + 59 - s

        if n not in answer:
            answer[n] = spent
        else:
            answer[n] += spent
            
    # 요금 계산
    for n, s in answer.items():
        if s >= fees[0]: # 기본 시간보다 오래 쓴 경우
            if (s - fees[0]) % fees[2] == 0:
                money = fees[1] + ((s - fees[0]) // fees[2]) * fees[3]
            else:
                money = fees[1] + ((s - fees[0]) // fees[2] + 1) * fees[3]
        else:
            money = fees[1]
        answer[n] = money

    answer = sorted(answer.items()) # 차량 번호가 작은 순으로 정렬
    for i in range(len(answer)):
        result.append(answer[i][1])

    return result


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
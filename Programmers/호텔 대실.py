def solution(book_time):
    answer = 0

    book_time.sort() # 시간복잡도: O(N)
    room = []

    for start, finish in book_time:
        sh, sm = map(int, start.split(':'))
        s = sh*60 + sm
        fh, fm = map(int, finish.split(':'))
        f = fh*60 + fm

        if room:
            cnt = 0
            for i in range(len(room)):
                if room[i][-1][-1] + 10 > s: # 아직 안나간 경우 새로운 리스트로 추가해야함
                    cnt += 1
                else:
                    room[i].append([s, f])
                    break

                if cnt == len(room):
                    room.append([[s, f]])
        else:
            room.append([[s, f]])

    return len(room)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
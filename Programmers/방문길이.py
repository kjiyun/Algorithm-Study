'''
주어진 방향대로 따라가면서 -5~5 사이의 범위 내에 존재하며, 방문한 적이 없는 횟수만 count
문제는 점으로 방문 여부를 체크하면 안됨, 선으로 체크

**한 점에서 이동할 때 방문 여부를 양방향으로 체크하기**
'''

def solution(dirs):
    answer = 0

    move = {'U':(-1, 0), 'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}
    v = [] #(x, y, 방향) 저장
     
    x, y = 0, 0  #시작위치
    for d in dirs:
        (dx, dy) = move[d]
        nx = x + dx
        ny = y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5 and [(x, y), (nx, ny)] not in v:
                answer += 1
                v.append([(x, y), (nx, ny)])  #방문처리
                v.append([(nx, ny), (x, y)])
                x = nx
                y = ny
        elif [(x, y), (nx, ny)] in v or [(nx, ny), (x, y)] in v:
            x = nx
            y = ny

    return answer

print(solution("URULDD"))
print(solution("ULURRDLLU"))
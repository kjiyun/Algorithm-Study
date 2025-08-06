# 내가 푼 방식
def solution(m, n, board):
    answer = 0 # 지워지는 블록의 갯수
    board = [list(x) for x in board]
    
    # 2x2형태를 모든 위치에서 확인 후 해당되면 set에 넣기
    while True:
        tmp = set()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] != [] and board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    tmp.add((i, j))
                    tmp.add((i+1, j))
                    tmp.add((i, j+1))
                    tmp.add((i+1, j+1))
                
        if len(tmp) == 0: # 더 이상 지울 게 없으면 종료
            break
        else:
            answer += len(tmp)
            for p, q in tmp:
                board[p][q] = [] # 빈칸으로 둠
            tmp = set() # 초기화
        
        # 블록 떨어짐
        while True:
            moved = 0
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == []:
                        board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
                        moved = 1
            if moved == 0:
                break
    return answer

# 다른 사람이 푼 방식
def solution(m, n, board):
    board.reverse()
    field = [list(cols) for cols in zip(*board)]
    answer = 0

    while True:
        bomb = set()
        for row in range(n - 1):
            for col in range(m - 1):
                try:
                    if field[row][col] == field[row + 1][col] == field[row][col + 1] == field[row + 1][col + 1]:
                        bomb.update({(row, col), (row + 1, col), (row, col + 1), (row + 1, col + 1)})
                except:
                    break

        if not len(bomb):
            break

        for r, c in bomb:
            field[r][c] = ''
            answer += 1

        for row in range(n):
            field[row] = list(''.join(field[row]))

    return answer
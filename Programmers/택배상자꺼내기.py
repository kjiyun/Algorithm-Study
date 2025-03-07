import sys
input = sys.stdin.readline

def solution(n, w, num):
    arr = [[0] * w for _ in range(n//w+1)]
    if n % w == 0:
        row = n // w
    else:
        row = n // w + 1 # 행의 수

    idx = 0
    for i in range(row):
        if i % 2 == 0: # 짝수 행인 경우
            for j in range(w):
                idx += 1
                arr[row-i-1][j] = idx
                print("kk:", arr[row-i-1][j])
                if idx == num:
                    a = row-i
                elif idx == n:
                    break
        else:
            for j in range(w):
                idx += 1
                arr[row-i-1][w-j-1] = idx
                print("dd:", arr[row-i-1][w-j-1])
                if idx == num:
                    a = row-i
                elif idx == n:
                    break
    
    answer = a
    print("arr:", arr)
    return answer

n, w, num = map(int, input().split())
print(solution(n, w, num))
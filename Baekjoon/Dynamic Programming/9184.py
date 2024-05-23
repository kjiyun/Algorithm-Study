# 신나는 함수 실행

wlist = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
# 0~20까지이므로 

def DP(a, b, c):
    if (a<=0 or b<=0 or c<=0):
        return 1
    if (a>20 or b>20 or c>20):
        return DP(20, 20, 20)
    # 만약에 배열에 이미 들어가 있으면 바로 출력
    if wlist[a][b][c]:
        return wlist[a][b][c]
    if (a<b<c):
        wlist[a][b][c] = DP(a, b, c-1) + DP(a, b-1, c-1) - DP(a, b-1, c)
        return wlist[a][b][c]
    else:
        wlist[a][b][c] = DP(a-1, b, c) + DP(a-1, b-1, c) + DP(a-1, b, c-1) - DP(a-1, b-1, c-1)
        return wlist[a][b][c]

while (True):
    a,b,c = map(int, input().split())
    if (a == -1 and b == -1 and c == -1):
        break
    print("w({}, {}, {}) = {}".format(a,b,c, DP(a,b,c)))
        # a, b, c = map(int, input().split())
        # x = tuple((a, b, c)) # 튜플 리스트에 저장 필요
        # print(x)
        # wlist.append(x)


#킹, 퀸, 룩, 비숍, 나이트, 폰

chess = [1, 1, 2, 2, 2, 8]
find = list(map(int, input().split()))

for i in range(len(find)):
    print(chess[i]-find[i], end=' ')
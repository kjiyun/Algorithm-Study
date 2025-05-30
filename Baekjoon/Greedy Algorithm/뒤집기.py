# 0과 1이 연속으로 나온 경우를 count해야한다고 생각
# 하지만, S의 길이가 100만보다 작은 매우 큰 수이기에 맞는 방법인지 고민..
# 그래도 이중 for문을 도는 게 아니므로 순차적으로 양옆만 비교하면서 이동

import sys
input = sys.stdin.readline

s = list(map(int, input().strip()))
a, b = 0, 0
if s[0] == 1:
    a += 1
elif s[0] == 0:
    b += 1
for i in range(1, len(s)):
    if s[i-1] == 1 and s[i] == 0:
        b += 1
    elif s[i-1] == 0 and s[i] == 1:
        a += 1
print(min(a, b))
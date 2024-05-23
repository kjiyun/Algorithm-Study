# 수 찾기

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a = sorted(a)

def find(low, high, target):
    if low > high: # 이 부분을 몰랐음
        return 0
    if target == a[(low+high)//2]:
        return 1
    elif target < a[(low+high)//2]:
        return find(low, (low+high)//2-1, target)
    else:
        return find((low+high)//2+1, high, target)

for i in b:
    print(find(0, m-1, i))   # 런타임 에러


# 다른 방법
from sys import stdin, stdout

n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')
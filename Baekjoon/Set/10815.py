#숫자 카드
import sys

n = sys.stdin.readline()
num = set(map(int, sys.stdin.readline().split()))

m = sys.stdin.readline()
find_num = list(map(int, sys.stdin.readline().split()))

for i in find_num:
    if i in num:
        print(1, end=" ")
    else:
        print(0, end=" ")
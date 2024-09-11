#회사에 있는 사람
import sys

n = int(sys.stdin.readline())
enter = set()

for i in range(n):
    name, act = sys.stdin.readline().split()
    if act == 'enter':
        enter.add(name)
    if act == 'leave':
        enter.remove(name)

enter = list(enter)
enter.sort(reverse=True)

for i in enter:
    print(i)
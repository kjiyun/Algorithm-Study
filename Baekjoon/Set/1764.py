#듣보잡
import sys

n, m = map(int, sys.stdin.readline().split())
hear = set()
hear_listen = set()

for _ in range(n):
    hear.add(sys.stdin.readline())

for _ in range(m):
    listen = sys.stdin.readline()
    if listen in hear:
        hear_listen.add(listen)

result = list(hear_listen)
result.sort()
print(len(result))
for i in result:
    print(i, end='')
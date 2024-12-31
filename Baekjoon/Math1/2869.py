# 달팽이는 올라가고 싶다.

a, b, v = map(int, input().split())
line = 0

if (v-b) % (a-b) == 0:
    line = (v-b) // (a-b)
elif (v-b) % (a-b) != 0:
    line = (v-b) // (a-b) + 1

print(line)
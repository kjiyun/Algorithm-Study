#직사각형에서 탈출

x, y, w, h = map(int, input().split())

distance = []

if x > (w-x):
    distance.append(w-x)
else:
    distance.append(x)

if y > (h-y):
    distance.append(h-y)
else:
    distance.append(y)

print(min(distance))

#간단한 방법
x, y, w, h = map(int, input().split())
print(min(x, w-x, y, h-y))
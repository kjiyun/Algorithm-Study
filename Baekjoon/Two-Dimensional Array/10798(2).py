# 세로 읽기

a = [[]*15]*5
length = []
word = ''

for i in range(5):
    a[i] = list(input())
    length.append(len(a[i]))

for i in range(max(length)):
    for j in range(5):
        if i < len(a[j]):
            word += a[j][i]

print(word)
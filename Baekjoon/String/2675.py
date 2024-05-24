# 문자열 반복

t = int(input())
num = []
words = []
for _ in range(t):
    r, s = input().split()
    num.append(r)
    words.append(s)

for i in range(t):
    for word in words[i]:
        print(word*int(num[i]), end='')
    print()

# 다른 방법 (입력하면서 한 줄씩 출력됨)
Case = int(input())

for i in range(Case):
    N, S = input().split()
    for j in range(len(S)):
        print(S[j] * int(N), end = '')
    print('')
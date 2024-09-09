#문자열 집합

n, m = map(int, input().split())
word_list = set()
result = 0

for i in range(n):
    word_list.add(input())

for i in range(m):
    check_word = input()
    if check_word in word_list:
        result += 1
print(result)
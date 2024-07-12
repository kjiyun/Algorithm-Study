# 그룹 단어 체커

n = int(input())
cnt = n

for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]: #바로 뒤의 문자와 다르면서 뒤의 문자들 중에 같은 문자가 존재하는 경우
            cnt -= 1
            break

print(cnt)
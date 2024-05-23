# 알파벳 찾기

s = list(input())
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 동일한 알파벳이 두 개 이상인 경우는 어떻게 처리하는가? 
# index는 두 번 이상 원소가 중복되어 존재하는 경웨 첫 원소의 인덱스를 출력한다.
for alph in alphabet:
    if alph in s:
        print(s.index(alph), end=' ')
    else:
        print('-1', end=' ')
print()


# 다른 방법 (find() 이용하기)
S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')
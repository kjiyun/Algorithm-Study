# 팰린드롬인지 확인하기

#1 컴파일 에러
word = input()
a = len(word)

for i in range(int(a/2)):
    if word[i] == word[a-1-i]:
        pass
    else:
        print(0)
        exit(0)   # exit(0): 프로그램 정상 종료 / exit(1): 프로그램 강제 종료
print(1)

#2 리스트의 슬라이싱 사용
word = list(input())

if word == word[::-1]:
    print(1)
else:
    print(0)

#3 reverse 함수 사용
word = list(input())

if word == list(reversed(word)):
    print(1)
else:
    print(0)
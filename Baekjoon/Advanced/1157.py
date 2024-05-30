# 단어 공부

word = input().upper()  # 대소문자 구분하지 않으므로 모두 대문자로 변경
word_list = list(set(word)) # 순서가 없는 집합 만들기
cnt = []

for i in word_list:
    count = word.count(i)  # 알파벳 개수 세기 위해 count 함수 사용
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))].upper())  #사용된 알파벳 개수를 이용하여 문자 출력
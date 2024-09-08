# 서로 다른 부분 문자열의 개수

s = input()
result = set()

for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        result.add(s[j:j+i])

print(len(result))

# result가 list인 경우
# tuple_result = [tuple(i) for i in result]
# print(len(set(tuple_result)))
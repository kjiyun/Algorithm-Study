#세로읽기

#오류남
#이유: 빈 배열을 칸 수에 맞게 만들어도 값을 배열에 집어넣으면 빈 배열의 값이 사라짐
arr = [[]*15 for _ in range(5)]
print('11', arr)

for i in range(5):
    arr[i] = list(input())
    print('arr', arr[i])

for i in range(15):
    for j in range(5):
        if arr[j][i]:
            print(arr[j][i], end='')

# 제출한 방법
arr = [[]*15 for _ in range(5)]
length = []
word = ''

for i in range(5):
    arr[i] = list(input())
    length.append(len(arr[i]))

for i in range(max(length)):
    for j in range(5):
        if i < len(arr[j]): 
            word += arr[j][i]
print(word)
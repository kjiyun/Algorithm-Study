#최댓값

#각 행의 최댓값을 구하고 각 행의 최댓값을 비교해서 제일 큰 수를 출력하기
#답은 올바르게 출력되었지만, 틀렸다고 함
#이유가 뭘까 ???
arr = [[0]*9 for _ in range(9)]
arr_max = [0]*9

for i in range(9):
    arr[i] = list(map(int, input().split()))
    arr_max[i] = max(arr[i])
    if (max(arr_max) == max(arr[i])):
        column = arr[i].index(max(arr[i]))+1

row = arr_max.index(max(arr_max))+1

print(max(arr_max))
print(row, column)

#다른 방법
table = [list(map(int, input().split())) for _ in range(9)]

max_num = 0
max_row, max_col = 0, 0
for row in range(9):
    for col in range(9):
        if max_num <= table[row][col]:
            max_row = row + 1
            max_col = col + 1
            max_num = table[row][col]

print(max_num)
print(max_row, max_col)
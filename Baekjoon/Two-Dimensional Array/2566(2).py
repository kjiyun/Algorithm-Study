#최댓값

a = []

for i in range(9):
    row = list(map(int, input().split()))
    a.append(row)

max_num = 0
max_row, max_col = 0, 0
for i in range(9):
    for j in range(9):
        if max_num <= a[i][j]:
            max_row = i+1
            max_col = j+1
            max_num = a[i][j]

print(max_num)
print(max_row, max_col)
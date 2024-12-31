# 분수 찾기

num = int(input())
line = 1
cnt = 1

while num > line:
    num -= line
    line += 1

if line % 2 == 0: # num이 분자, (line+1)-num이 분모
    a = num
    b = line+1-num
elif line % 2 == 1:
    a = line+1-num
    b = num

print(f'{a}/{b}')
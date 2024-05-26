# 다이얼

call = list(input())
call_num = []

for i in call:
    if i in 'ABC':
        call_num.append(2)
    elif i in 'DEF':
        call_num.append(3)
    elif i in 'GHI':
        call_num.append(4)
    elif i in 'JKL':
        call_num.append(5)
    elif i in 'MNO':
        call_num.append(6)
    elif i in 'PQRS':
        call_num.append(7)
    elif i in'TUV':
        call_num.append(8)
    elif i in 'WXYZ':
        call_num.append(9)

print(sum(call_num)+len(call_num))

# if i == 'A' or 'B' or 'C: 로 하는 경우 인식 못함!

# 다른 방법
LS = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

S = input()
time = 0

for s in S:
    for i in LS:
        if s in i:
            print(s, i)
            time += LS.index(i) + 3
print(time)
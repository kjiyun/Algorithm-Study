# 도키도키 간식드리미**

n = int(input())  #승환이 앞에 서있는 학생 수

line = list(map(int, input().split()))  #현재 줄 서있는 곳
tmp = []  #임시 대기줄
target = 1

while line:
    if line[0] == target: #순서에 맞는 번호라면
        line.pop(0)  #첫번째 원소가 나옴
        target += 1
    else:
        tmp.append(line.pop(0)) #줄에서 제거하면서 임시 대기줄에 추가

    while tmp:
        if tmp[-1] == target:
            tmp.pop()  #마지막 원소가 나옴
            target += 1
        else:
            break

if len(tmp) == 0:
    print("Nice")
else:
    print("Sad")
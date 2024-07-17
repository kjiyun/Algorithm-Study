#너의 평점은

# dict 형태로 저장하고 key값에 해당하는 value를 얻을 것
score = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
sub_sum = 0.0
sub_credit = 0.0
subject_list = [[0]*3 for _ in range(20)]

for i in range(20):
    subject = input().split()
    subject_list[i] = subject

    if (subject_list[i][2] != 'P'):  #등급이 P인 경우 계산에서 제외해야 한다.
        sub_sum += float(subject_list[i][1]) * float(score[subject_list[i][2]])
        sub_credit += float(subject_list[i][1])

print(sub_sum/sub_credit)
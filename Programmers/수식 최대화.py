'''
num_list[i+1], op_list[i]를 제거해야 하는데 이 부분을 생각 못함 
위의 값을 제거하면 그 다음 인덱스가 한 칸 당겨지므로 i는 그대로 둬야함
-> i를 for문 돌리지 않고 if문으로 돌리기
'''

from itertools import permutations
import copy

def calculate(n1, n2, c):
    if c == '*':
        return n1 * n2
    elif c == '+':
        return n1 + n2
    elif c == '-':
        return n1 - n2

def solution(expression):
    
    op = ['*', '+', '-']
    idx = 0
    num_list = []
    op_list = []
    for i in range(len(expression)):
        if expression[i] in op:
            num_list.append(int(expression[idx:i]))
            idx = i+1
            op_list.append(expression[i])
    num_list.append(int(expression[idx:]))
    
    max_num = -1e9
    for order in permutations(op, 3):
    # order = ('*', '+', '-')
        tmp_num = copy.deepcopy(num_list)
        tmp_op = copy.deepcopy(op_list)

        for o in order:
            i = 0
            while i < len(tmp_op):
                if tmp_op[i] == o:
                    tmp = calculate(tmp_num[i], tmp_num[i+1], o)
                    tmp_num[i] = tmp
                    del tmp_num[i+1]
                    del tmp_op[i]
                else:
                    i += 1
                
        for t in tmp_num:
            if max_num < abs(t):
                max_num = abs(t)
    return max_num
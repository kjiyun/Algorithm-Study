#좌표 압축
import sys

n = int(sys.stdin.readline())

x_arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(set(x_arr)) #중복제거

dic = {arr[i]:i for i in range(len(arr))}

for i in x_arr:
    print(dic[i], end=' ')
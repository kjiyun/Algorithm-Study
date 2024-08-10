#세막대

stick = list(map(int, input().split()))

if max(stick) < (sum(stick)-max(stick)):
    print(sum(stick))
else:
    print((sum(stick)-max(stick))*2-1)
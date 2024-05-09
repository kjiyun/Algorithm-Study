# 파도반 수열

# p[n] = p[n-2] + p[n-3]

t = int(input())

for _ in range(t):
    n = int(input())

    p = [0] * (101)

    p[1] = 1
    p[2] = 1
    p[3] = 1
    
    if (n > 3):
        for i in range(4, n+1):
            p[i] = p[i-3] + p[i-2]
    print(p[n])

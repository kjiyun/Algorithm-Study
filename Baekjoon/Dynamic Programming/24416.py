# 알고리즘 수업 - 피보나치 수 1

n = int(input())
num1 = 0
num2 = 0

def fib(n):
    global num1  # 전역변수 선언을 해줘야 함

    if (n==1 or n==2):
        num1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibonacci(n):
    global num2

    f = [0]*n
    for i in range(n):
        if (i==1 or i==2):
            f[i] = 1
        else:
            num2 += 1
            f[i] = f[i-1] + f[i-2]
    return f

fib(n)
fibonacci(n)
print(num1, num2)
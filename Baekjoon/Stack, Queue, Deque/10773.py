#제로

k = int(input())
stack = []

for _ in range(k):
    money = int(input())
    if money != 0:
        stack.append(money)
    elif money == 0:
        stack.pop()

print(sum(stack))
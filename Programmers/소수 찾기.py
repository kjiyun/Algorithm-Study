from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):
        for j in permutations(list(numbers), i):
            num = int(''.join(j))
            for k in range(2, num):
                if num % k == 0:
                    break
                elif num == k+1 and num not in answer and num != 0 and num != 1:
                    answer.append(num)

    print(answer)
    return len(answer)

numbers = "011"
print(solution(numbers))
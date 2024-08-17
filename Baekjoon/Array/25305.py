#커트라인

n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

print(arr[-k])
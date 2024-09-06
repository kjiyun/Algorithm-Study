#대칭 차집합

a, b = map(int, input().split())

a_list = set(list(map(int, input().split())))
b_list = set(list(map(int, input().split())))

# for i in a_list:
#     if i in b_list:
#         a_list.remove(i)

# for j in b_list:
#     if j in a_list:
#         b_list.remove(j)
#         continue

print(len(a_list-b_list)+len(b_list-a_list))
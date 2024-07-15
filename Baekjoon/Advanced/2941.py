# 크로아티아 알파벳

word = input()
new = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in new:
    word = word.replace(i, '*')

print(len(word))
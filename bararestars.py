n, m = input().split()
e = []
star = 0
for i in range(0, int(n)):
    a = input()
    e.append(a)
for i in e:
    for j in i:
        if j == '*':
            star += 1
print(star)
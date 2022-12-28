a = int(input())
e = []
for i in range(a):
    b = input().split()
    for i in b:
        c = i.lower()
        c = c.capitalize()
        e.append(c)
    e.append('/')
for i in e:
    if i == '/':
        print('')
    else:
        print(i, end = ' ')    
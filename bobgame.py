a, b = input().split()
k = int(input())
e = []
for i in range(0, k):
    c = input().split()
    for j in range(0, 2):
        c[j] = int(c[j])
    e.append(c)
print(e)
q = []
for i in range(1, int(a) + 1):
    for j in range(1, int(b) + 1):
        f = [i, j]
        if f in e:
            print('*', end = ' ')
            q.append('*')
        else:
            print('2', end = ' ')
            q.append('2')
    print()
print(q)
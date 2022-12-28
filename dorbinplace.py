a = input().split()
b = input().split()
c = input().split()
t = [a[0], b[0], c[0]]
ar = [a[1], b[1], c[1]]
i = 0
e = []
if t[0] == t[2]:
    e.append(t[1])
    if ar[0] == ar[2]:
        e.append(ar[1])
    elif ar[0] == ar[1]:
        e.append(ar[2])
    elif ar[1] == ar[2]:
        e.append(ar[0])
elif t[0] == t[1]:
    e.append(t[2])
    if ar[0] == ar[2]:
        e.append(ar[1])
    elif ar[0] == ar[1]:
        e.append(ar[2])
    elif ar[1] == ar[2]:
        e.append(ar[0])
elif t[2] == t[3]:
    e.append(t[0])
    if ar[0] == ar[2]:
        e.append(ar[1])
    elif ar[0] == ar[1]:
        e.append(ar[2])
    elif ar[1] == ar[2]:
        e.append(ar[0])
print(' '.join(e))
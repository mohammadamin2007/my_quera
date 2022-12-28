a = int(input())
e = []
for i in range(0, a):
    b = int(input())
    e.append(b)
q = e[0]
w = 0
for i in e:
    if q == i + 1 or q == i - 1:
        w += 1
        q = i
    else:
        q = i
print(w)
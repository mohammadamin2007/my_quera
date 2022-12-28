a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
d1, e1, f1 = [], [], []
d = input().split()
for i in range(int(d[0]), int(d[1])):
    d1.append(i)
e = input().split()
for i in range(int(e[0]), int(e[1])):
    e1.append(i)
f = input().split()
for i in range(int(f[0]), int(f[1])):
    f1.append(i)
sum = 0
d1 = set(d1)
f1 = set(f1)
e1 = set(e1)
an = d1 & e1 & f1
sum += len(an) * c * 3
an = d1 - e1 - f1
an2 = e1 - d1 - f1
an3 = f1 - d1 - e1
e = [an, an2, an3]
for i in e:
    sum += len(i) * a
an = d1 & e1
an2 = d1 & f1
an3 = e1 & f1
e = an ^ an2 ^ an3 - d1 & e1 & f1
sum += len(e) * 2 * b
print(sum)
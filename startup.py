a, b, c, d = input().split()
a, b, c, d = int(a), int(b), int(c), int(d)
a1, b1, c1, d1 = 0, 0, 0, 0
while True:
    a -= 1
    if a != 0:
        a1 += 1
    else: 
        break
    b -= 1
    if b != 0:
        b1 += 1
    else:
        break
    c -= 1
    if c != 0:
        c1 += 1
    else:
        break
    d -= 1
    if d != 0:
        d1 += 1
    else:
        break
print(a1, b1, c1, d1)
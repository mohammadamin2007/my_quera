a = int(input())
b = int(input())
c = int(input())
e = [a, b, c]
e.sort()
if e[0] ** 2 + e[1] ** 2 == e[2] ** 2:
    print('YES')
else:
    print('NO')
n, l = input().split()
n, l = int(n), int(l)
e = []
for i in range(0, int(n)):
    a = int(input())
    e.append(a)
sumx = sum(e)
if sumx >= l:
    print('YES')
else:
    print('NO')
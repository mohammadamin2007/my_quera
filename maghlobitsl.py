a = input()
b = int(a)
e = []
for i in a:
    e.append(i)
e.reverse()
a = ''.join(e)
if int(a) == b:
    print('YES')
else:
    print('NO')
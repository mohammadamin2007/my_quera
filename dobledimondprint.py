a = int(input())
p = 1
if a == 5:
    w = 2
else:
    w = 2
    q = (a - 5)//2
    w += q
for i in range(1, a, 2):
    print(' ' * (w - i  + p), end = '')
    print('*' * i, end = '')
    print(' ' * 2 *(w - i  + p), end = '')
    print('*' * i, end = '')
    print()
    p += 1
print('*'* 2 * a)
if a == 5:
    w = 2
    p = 2
else:
    w = 2
    q = (a - 5)//2
    w += q
    p = w
for i in range(a -  2, 0, -2):
    print(' ' * (w - i  + p), end = '')
    print('*' * i, end = '')
    print(' ' * 2 *(w - i  + p), end = '')
    print('*' * i, end = '')
    print()
    p -= 1
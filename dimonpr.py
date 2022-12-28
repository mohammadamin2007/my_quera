a = int(input())
for i in range(0, a):
    n = (2 * i) + 1
    w = a  - i
    print(' ' * w, end = '')
    print('*' * n)
n = 2 * a + 1
print('*' * n)
for i in range(a - 1, 0 - 1, -1):
    n = (2 * i) + 1
    w = a  - i
    print(' ' * w, end = '')
    print('*' * n)
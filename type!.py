a = input()
c = a.count('=')
b = a.split(c * '=')
d = list(b[0])
for i in range(1, c + 1):
    del d[-1]
d = ''.join(d)
print(d, end = '')
print(b[1], end = '')
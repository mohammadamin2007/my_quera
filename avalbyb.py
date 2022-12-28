a = int(input())
b = int(input())
def isaval(i):
        a = []
        for j in range(1, i + 1):
            if i % j == 0:
               a.append(j)
        if len(a) == 2:
            return 'true'
        else:
            return 'false'
e = []
for i in range(a + 1, b):
    if isaval(i) == 'true':
        e.append(str(i))
print(','.join(e))
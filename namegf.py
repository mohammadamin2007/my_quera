a = int(input())
e = []
for i in range(0, a):
    b = input()
    e.append(b)
def count2(a):
    b = [a[0]]
    for i in a:
        for j in b:
            if i != j:
                t ='true'
            elif i == j:
                t = 'false'
                break
        if t == 'true':
            b.append(i)
    return len(b)
res = 0
for i in e:
    b = count2(i)
    if b > res:
        res = b
print(res)
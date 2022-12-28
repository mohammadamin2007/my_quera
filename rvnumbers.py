e = []
while True:
    a = int(input())
    if a == 0:
        break
    else:
        e.append(a)
e.reverse()
for i in e:
    print(i)
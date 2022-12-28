a = int(input())
e = []
for i in range(a):
    b = input()
    e.append(b)
i = 0
while i < len(e):
    if e[i] == 'CAPS':
        j = i + 1
        while True:
            if j != len(e):
                if e[j] == 'CAPS':
                    i = j + 1
                    break
                else:
                    print(e[j].upper(), end = '')
                j += 1
            else:
                i = j
                break
    else:
        print(e[i], end = '')
        i += 1
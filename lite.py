b = input()
y = 0
r = 0
g = 0
for i in b:
    if i == 'G':
        g += 1
    elif i == 'R':
        r += 1
    elif i == 'Y':
        y += 1
if r >= 3:
    print('nakhor lite')
elif r == 5 or y == 5:
    print('nakhor lite')
elif r >= 2 and y >= 2:
    print('nakhor lite')
else:
    print('rahat baash')
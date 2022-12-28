e = []
for i in range(0, 5):
    a = input()
    e.append(a)
h = 'HAFEZ'
m = 'MOLANA'
i = 0
w = []
while i < len(e):
    if h in e[i]:
        w.append(i)
    elif m in e[i]:
        w.append(i)
    i += 1
if len(w) == 0:
    print('NOT FOUND!')
else:
    for i in w:
        print(i + 1, end = ' ')

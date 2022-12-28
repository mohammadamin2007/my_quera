a = input().split()
b = input().split()
i = 0
while i < len(a):
    a[i], b[i] = int(a[i]), int(b[i])
    i += 1
if a[0] > b[0] and a[1] > b[1]:
    print('yes')
elif a[0] == b[0] and a[1] == b[1]:
    print('yes')
elif a[0] == b[0] and a[1] > b[1]:
    print('yes')
elif a[0] > b[0] and a[1] == b[1]:
    print('yes')
else:
    print('no')
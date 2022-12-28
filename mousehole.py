a, b = input().split()
a, b = int(a), int(b)
if a == b:
    print('Saal Noo Mobarak!')
else:
    w = b - a
    if w > 0:
        for i in range(0, w):
            print('R', end = '')
    elif w < 0:
        w = w * -1
        for i in range(0, w):
            print('L', end = '')
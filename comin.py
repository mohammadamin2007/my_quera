r, c = input().split()
r, c = int(r), int(c)
if 1 <= c <= 10:
    print('Right', end = ' ')
    placer = (10 - r) + 1
    print(placer, end = ' ')
    print(c, end = '')
elif 10 <= c <= 20:
    print('Left', end = ' ')
    placer2 = (10 - r) + 1
    print(placer2, end = ' ')
    placec = (20 - c) + 1
    print(placec, end = '')    
a = input().split()
shah = int(a[0])
vasir = int(a[1])
rokh = int(a[2])
fil = int(a[3])
asbe = int(a[4])
sarbaz = int(a[5])
if shah != 1:
    if shah == 0:
        print(1, end = ' ')
    elif shah > 1:
        print(-1 * (shah -1), end = ' ')
elif shah == 1:
    print(0, end = ' ')
if vasir != 1:
    if vasir == 0:
        print(1, end = ' ')
    elif vasir > 1:
        print(-1 * (vasir -1), end = ' ')
elif vasir == 1:
    print(0, end = ' ')
if rokh != 2:
    if rokh < 2:
        print(2 - rokh, end = ' ')
    elif rokh > 2:
        print(-1 * (rokh - 2), end = ' ')
elif rokh == 2:
    print(0, end = ' ')
if fil != 2:
    if fil < 2:
        print(2 - fil, end = ' ')
    elif fil > 2:
        print(-1 * (fil - 2), end = ' ')
elif fil == 2:
    print(0, end = ' ')
if asbe != 2:
    if asbe < 2:
        print(2 - asbe, end = ' ')
    elif asbe > 2:
        print(-1 * (asbe - 2), end = ' ')
elif asbe == 2:
    print(0, end = ' ')
if sarbaz != 8:
    if sarbaz < 8:
        print(8 - sarbaz, end = '')
    elif sarbaz > 2:
        print(-1 * (sarbaz - 8), end = '')
elif sarbaz == 8:
    print(0, end = '')
a, b = input().split()
a, b = int(a), int(b)
mainhour = 12 - a
mainmin = 60 - b
if mainhour < 10:
    print(f'0{mainhour}:',end = '')
else:
    if mainhour == 12:
        print(f'{0}{0}:', end = '')
    else:
        print(f'{mainhour}:',end = '')
if mainmin < 10:
    print(f'0{mainmin}',end = '')
else:
    if mainmin == 60:
        print('00', end = '')
    else:
        print(mainmin, end = '')

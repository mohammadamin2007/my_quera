a = int(input())
for i in range(0, a + 1):
    if i == 0:
        print('*' * a)
    elif i == a:
        print('*' * a)
    else:
        if i != 2:
            for j in range(1, a  + 1):
                if j == 1:
                    print('*', end = '')
                elif j == a:
                    print('*', end = '')
                else:
                    print(' ', end = '')
            print('')
    
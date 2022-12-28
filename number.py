a = input()
for i in a:
    print(f'{i}: ', end = '')
    for j in range(int(i)):
        print(i, end = '')
    print('')
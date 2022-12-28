a = int(input())
e = []
if a == 1 or a == 0:    
    print('YES')
else:
    for i in range(1, a):
        if a % i == 0:
            if i != a:
                e.append(i)
    sum = 0
    for i in e:
        sum += i
    if sum == a:
        print('YES')
    else:
        print('NO')

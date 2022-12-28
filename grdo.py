n, x, y = input().split()
n, x, y = int(n), int(x), int(y)
i = 1
sum = 0
if x + y > n:
    print(-1)
else:
    if n % x == 0:
        print(n // x, 0)
    elif n % y == 0:
        print(0, n // y)
    else:
        while sum != n:
            sum = i * x
            p = n - sum
            if p % y == 0:
                print(i,(n - sum)// y)
                break
            i += 1       
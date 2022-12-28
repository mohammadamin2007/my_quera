a, b = input().split()
i = 1
while True:
    w = i * int(b) % int(a)
    if 0 <= w <= int(a) / 2 :
        print(i * int(b))
        break
    i += 1
a, b, l = input().split()
start = int(a) + 0
for i in range(2, int(l) + 1):
    if i % 2 == 0:
        start += int(b)
    else:
        start += int(a)
print(start)

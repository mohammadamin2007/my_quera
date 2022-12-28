m, n = input().split()
m, n = int(m), int(n)
i = 0
while m > 1:
    m -= n
    i += 1
print(i)
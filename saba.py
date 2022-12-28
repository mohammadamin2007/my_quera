from math import floor
n, k = input().split()
n, k = int(n), int(k)
for i in range(0, k):
    n /= 2
print(floor(n))
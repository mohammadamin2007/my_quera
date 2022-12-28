n, x, k = input().split()
n, x, k = int(n), int(x), int(k)
e = []
for i in range(n):
    a = input()
    e.append(a)
i = x
j = 0
while j < k:
    if i == n:
        i = 1
    else:
        i += 1
    j += 1
print(e[i - 1]) 
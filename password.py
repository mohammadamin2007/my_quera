a = int(input())
b = input()
e = []
for i in range(a):
    c = input()
    e.append(c)
i = 0
result = []
while i < len(b):
    j = 0
    p = e[i]
    while j < len(p):
        if p[j] == b[i]:
            result.append(j)
            break
        j += 1
    i += 1
sum = 0
for i in result:
    if i > 4:
        sum += 9 - i
    else:
        sum += i
print(sum)
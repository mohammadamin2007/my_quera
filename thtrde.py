a = int(input())
def devisor(i):
    e = []
    for j in range(1, i + 1):
        if i % j == 0:
            e.append(j)
    return e
sumx = 0
l = 0
for i in range(1, a + 1):
    e = devisor(i)
    sumx += sum(e)
    l +=len(e)
print(l ,sumx)
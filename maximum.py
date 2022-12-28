b = int(input())
a = input().split()
i = 0
while i < len(a):
    a[i] = int(a[i])
    i += 1
def maxx(a):
    max = a[0]
    for i in a:
        if i > max:
            max = i
    return max
print(maxx(a))

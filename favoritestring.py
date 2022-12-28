a = input()
b = int(input())
e = []
for i in range(0, b):
    c = input()
    if a in c:
        e.append('Yes')
    else:
        e.append('No')
print(e.count('Yes'))
a = int(input())
a1 = input().split()
b = int(input())
b1 = input().split()
c = int(input())
c1 = input().split()
e = []
for i in b1:
    for j in a1:
        if i == j:
            y = 'y'
            break
        else:
            y = 'n'
    if y == 'n':
        a1.append(i)
for i in c1:
    for j in a1:
        if i == j:
            y = 'y'
            break
        else:
            y = 'n'
    if y == 'n':
       a1.append(i)
weekdays = ['shanbe', '1shanbe', '2shanbe', '3shanbe', '4shanbe', '5shanbe', 'jome']
result = []
for i in weekdays:
    for j in a1:
        if j == i:
            y = 'y'
            break
        else:
            y = 'n'
    if y == 'n':
        result.append(i)
print(len(result))
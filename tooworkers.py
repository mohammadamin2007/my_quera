a = int(input())
e = []
for i in range(0, a):
    b = input().split()
    e.append(b[0])
r = list(dict.fromkeys(e))
numbers = []
for i in r:
    numbers.append(e.count(i))
print(max(numbers))
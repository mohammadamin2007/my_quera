a, b = input().split()
a, b = int(a), int(b)
botels = input().split()
sumbt = 0
for i in botels:
    sumbt += int(i)
total = a * b
t = total - sumbt
result = t // b
print(result)
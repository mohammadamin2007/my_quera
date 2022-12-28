n = int(input())
a = input().split()
b = input().split()
i = 0
sum = 0
while i < len(a):
    nafas = int(a[i]) * int(b[i])
    sum += nafas
    i += 1
print(sum)
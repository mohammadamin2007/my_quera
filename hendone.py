a = int(input())
b = input().split()
for i in range(0, len(b)):
    b[i] = int(b[i])
c = max(b)
i = 0
while i < len(b):
    if b [i] == c:
        print(i + 1)
        break
    i += 1
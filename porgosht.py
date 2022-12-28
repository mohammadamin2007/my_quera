n, m = input().split()
sum = [0, 0]
for i in range(0, 2):
    for j in range(0, int(n)):
        b = input()
        v = b.count('*')
        sum[i] += v
print(sum[0], sum[1])
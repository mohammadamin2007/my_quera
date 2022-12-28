e = []
for i in range(0, 4):
    a = int(input())
    e.append(a)
sum = 0
for i in e:
    sum += int(i)
print('Sum :','{0:6f}'.format(sum))
print('Average :','{0:6f}'.format(sum/4))
prod = 1
for i in e:
    prod *= i
print('Product :','{0:6f}'.format(prod))
print('MAX :','{0:6f}'.format(max(e)))
print('MIN :','{0:6f}'.format(min(e)))
len = int(input())
num = input().split()
print(num)
for i in range(0, len):
    if i == 0:
        if int(num[i]) > int(num[i + 1]) and int(num[i]) > int(num[i + 2]):
            print('Ey baba :(')
            break
    elif i == len - 1:
        print('Bah Bah! Ajab jooji!')
    else:
        if int(num[i]) > int(num[i - 1]) and int(num[i]) > int(num[i + 1]):
            print('Ey baba :(')
            break
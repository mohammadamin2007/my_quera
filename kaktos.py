a = int(input())
b = input().split()
for i in b:
    if int(i) > 3:
        print('*')
    else:
        print('*' * int(i))
a = input()
b = input()
a1 = a[::-1]
b1 = b[::-1]
if int(a1) > int(b1):
    print(int(b),'<',int(a))
elif int(a1) < int(b1):
    print(int(a),'<',int(b))
else:
    print(int(a),'=',int(b))
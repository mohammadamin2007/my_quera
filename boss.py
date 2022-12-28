x1, y1, x2, y2 = input().split()
if int(x1) == int(x2):
    print('Vertical')
elif int(y1) == int(y2):
    print('Horizontal')
else:
    print('Try again')
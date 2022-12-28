n = input()
b = 0
for i in n:
    b += int(i)
w = 0
def isaval(i):
    y = 'n'
    if i > 1: 
        for j in range(2, i): 
            if i % j == 0: 
                y = 'n'
                break
            else: 
                y = 'y'
    else: 
       return 'false'
    if y == 'y':
        return 'True'
    else:
        return 'false'
i = int(n) + 1
while True:
    if isaval(i) == 'True':
        w += 1
        if w == b:
            print(i)
            break
    i += 1
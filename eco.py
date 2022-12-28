a = input()
e = []
for i in a:
    e.append(i)
i = 0
while i < len(e):     
    j = 0    
    while j <= i:
        e[j] = e[i]
        j += 1
    q = ''.join(e)
    print(q)
    i += 1
a = input()
hafez = 'HAFEZ'
molana = 'MOLANA'
def find(order, string):
    e = []
    for i in string:
        for j in order:
            if i == j:
                e.append(i)
                break
    if ''.join(e) == order:
        return 'y'
    else:
        print(e)
        return 'n'
find(hafez, a)
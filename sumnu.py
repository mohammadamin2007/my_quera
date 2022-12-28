a = input()
def sum(a):
    suma = 0
    for i in a:
        suma += int(i)
    if len(str(suma)) == 1:
        return suma
    else:
        return sum(str(suma))
print(sum(a))
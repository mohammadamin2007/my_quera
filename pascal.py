from math import factorial as fact 

def number(n, k):
    number = fact(n) / (fact(k) * fact(n-k))
    return number
def pascal_triangle(n):
    row_list = []
    for row in range(n):
        for k in range(row+1):
            number1 = number(row, k)
            row_list.append(int(number1))
        for i in row_list:
            print(i, end = ' ')
        print()
        row_list.clear()
n = int(input())
 
pascal_triangle(n)
 
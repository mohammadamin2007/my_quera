#a='N'
def z(n):
    if n==1:
        print('Yes')
    else:
        if n%2==0:
            n//=2
        else:
            n=3*n+3
        if n!=3:
            z(n)
        else:
            print('No')
    return n
n=int(input())
b = z(n)
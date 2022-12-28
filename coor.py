t = int(input())
str = input()
str2 = input()
eshtebah = 0
for i in range(0, t):
    if str[i] != str2[i]:
        eshtebah += 1
print(eshtebah)

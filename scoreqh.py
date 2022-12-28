x = int(input())
n = int(input())
if 0 <= x <= 20:
    if n == 0:
        print(20)
    elif n == 7:
        print(x)
    else:
        score = x - n
        if score <= 0:
            print(0)
        elif score >= 0:
            print(score)

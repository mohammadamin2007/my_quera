wi = float(input())
hi = float(input())
bmi = wi / hi ** 2
print('{0:<8.2f}'.format(bmi))
if bmi < 18.5:
    print('Underweight')
elif 18.5 <= bmi < 25:
    print('Normal')
elif 25 <= bmi < 30:
    print('Overweight')
elif 30 <= bmi:
    print('Obese')
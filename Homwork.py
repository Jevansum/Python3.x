# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
BMI = weight/height**2
if BMI < 18.5:
    print('过轻:',BMI)
elif 18.5 <= BMI < 25:
    print('正常:',BMI)
elif 25 <= BMI < 28:
    print('过重:',BMI)
elif 28 <= BMI < 32:
    print('肥胖:',BMI)
elif BMI > 35:
    print('严重肥胖:',BMI)


L = ['Bart', 'Lisa', 'Adam']
Li = 0
while Li < len(L):
    print('Hello, %s!'%L[Li])
    Li = Li +1

for Ln in L:
    print('Hello, %s!'%Ln)
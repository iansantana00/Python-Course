# -*- Coding: uft-8 -*-
print ('EQUAÇÃO DO SEGUNDO GRAU')
print ('-----------------------')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
print (a, 'x2 + ',b ,'x + ', c, ' = 0')

Delta = (b**2) - (4 * a * c)

if Delta < 0:
    print ('Delta negativo')
else:
    x1 = (b + (Delta**1/2))/2*a
    x2 = (-b - (Delta**1/2))/2*a
    print ('As raízes são', x1, 'e', x2)


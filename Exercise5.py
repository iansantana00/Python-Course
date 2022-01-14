# -*- Coding: uft-8 -*-
v1 = float(input('Digite um valor: '))
s = input ("Digite um sinal: ")
v2 = float(input('Digite outro valor: '))
print ('OPERANDO..')
if s == '+':
   print (v1 + v2)
elif s == '-':
   print (v1 - v2)
elif s == '*':
   print (v1 * v2)
elif s == '/':
   print (v1 / v2)
elif s == '**':
   print (v1 ** v2)
else:
   print ('SINAL INVÁLIDO!')

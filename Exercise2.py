# -*- Coding: uft-8 -*-
print ('        BOLETIM       ')
print ('-------------------------')
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
media = (nota1 + nota2) / 2
print ('Sua media é ', media)
if media >= 6:
    print ('PARABÉNS, VOCÊ FOI APROVADO!')
else:
    print ('REPROVADO!')

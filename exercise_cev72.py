
tupla = ('zero', 'um', 'dois', 'três',' quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoite', 'dezenove', 'vinte')

numero = - 1

while numero < 0 or numero > 20:
    numero = int(input('Digite um número inteiro entre 0 e 20: '))
    if numero >= 0 and numero <= 20:
        print(f'Você digitou o número {tupla[numero]}.')
    else:
        print('Tente novamente.')

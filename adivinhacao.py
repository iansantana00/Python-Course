
print('*'*24)
print('*', ''*3, 'Jogo da Adivinhação', ''*3, '*')
print('*'*24)

numero_secreto = 42

chute = int(input('Digite o seu número: '))
print(f'Você digitou {chute}')

if(numero_secreto == chute):
    print('Você acertou!')
else:
    print('Você errou! ')

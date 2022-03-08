from random import choice as escolha

objeto = ['pedra', 'papel', 'tesoura']

ian = input('Ian: Vou escolher ')
ian = ian.lower() 

while ian != 'pedra' and ian != 'tesoura' and ian != 'papel':
    ian = input('Ian: Vou escolher ')

junior = escolha(objeto)

resultado = []

print(f'Ian: {ian}')
print(f'Junior: {junior}')

if ian == junior:
    resultado = 'Empate'
elif ian == 'pedra' and junior == 'tesoura':
    resultado = 'Ian venceu'
elif ian == 'pedra' and junior == 'papel':
    resultado = 'Junior venceu'
elif junior == 'pedra' and ian == 'tesoura':
    resultado = 'Junior venceu'
elif junior == 'pedra' and ian == 'papel':
    resultado = 'Ian venceu'
elif ian == 'papel' and junior == 'tesoura':
    resultado = 'Junior venceu'
elif ian == 'tesoura' and junior == 'papel':
    resultado = 'Ian venceu'


print(f'RESULTADO: {resultado}!')
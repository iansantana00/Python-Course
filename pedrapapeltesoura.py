from random import choice as escolha

objeto = ['Pedra', 'Papel', 'Tesoura']

ian = escolha(objeto)
junior = escolha(objeto)

resultado = []

print(f'Ian: {ian}')
print(f'Junior: {junior}')

if ian == junior:
    resultado = 'Empate'
elif ian == 'Pedra' and junior == 'Tesoura':
    resultado = 'Ian venceu'
elif ian == 'Pedra' and junior == 'Papel':
    resultado = 'Junior venceu'
elif junior == 'Pedra' and ian == 'Tesoura':
    resultado = 'Junior venceu'
elif junior == 'Pedra' and ian == 'Papel':
    resultado = 'Ian venceu'
elif ian == 'Papel' and junior == 'Tesoura':
    resultado = 'Junior venceu'
elif ian == 'Tesoura' and junior == 'Papel':
    resultado = 'Ian venceu'


print(f'RESULTADO: {resultado}!')
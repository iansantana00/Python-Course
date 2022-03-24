import adivinhacao
import forca

print('********************************')
print('*********MENU DE JOGOS**********')
print('********************************')
print('1. Adivinhação')
print('2. Forca')

escolha = int(input('Qual jogo quer jogar? Digite o número: '))

if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2:
    forca.jogar()

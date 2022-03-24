from random import choice as escolha


def jogar():

    numeros: int = range(0, 11)

    print('*'*24)
    print('*', ''*3, 'Jogo da Adivinhação', ''*3, '*')
    print('*'*24)
    print('Você deve adivinhar um número de 0 a 10')

    dificuldade = input('Deseja jogar em qual nível (fácil, médio, difícil)? ')

    if dificuldade == 'fácil':
        total_de_tentativas = 4
    elif dificuldade == 'médio':
        total_de_tentativas = 3
    elif dificuldade == 'difícil':
        total_de_tentativas = 2

    numero_secreto = escolha(numeros)
    rodada: int = 1

    for rodada in range(1, total_de_tentativas):

        print(f'Tentativa {rodada} de {total_de_tentativas}')

        chute = int(input('Digite o seu número: '))
        print(f'Você digitou {chute}')

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print('Você acertou!')
            break
        elif maior:
            print('Você errou! O seu chute foi maior que o número secreto')
        elif menor:
            print('Você errou! O seu chute foi menor que o número secreto')

    print(f'O número secreto era {numero_secreto}')
    print('*******Fim de Jogo*******')

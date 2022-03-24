import random

erros = 0


def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    acertou = False
    enforcou = False
    erros = 0

    while not enforcou and not acertou:

        chute = pede_chute()

        if chute in palavra_secreta:
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)

        else:
            erros += 1

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


def imprime_mensagem_abertura():
    print('********************************')
    print('***Bem vindo ao jogo da forca***')
    print('********************************')


def carrega_palavra_secreta():
    with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
        palavras = []

        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    return ['_' for letra in palavra_secreta]


def pede_chute():
    chute = input('Qual a letra? ')
    chute = chute.strip().upper()
    return chute


def marca_chute_correto(chute, palavra_secreta, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        acertou = '_' not in letras_acertadas
        enforcou = erros == 6
        if chute.upper() == letra.upper():
            print(f'Encontrei a letra {letra} na posição {posicao}')
            letras_acertadas[posicao] = letra
        posicao += 1


def imprime_mensagem_vencedor():
    print('Você ganhou!')


def imprime_mensagem_perdedor():
    print('Você perdeu!')

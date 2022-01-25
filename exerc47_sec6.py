
r = 0

while r != '5':

    print('-------CALCULADORA INTELIGENTE-------')

    print('OPÇÃO 1: Adição')
    print('OPÇÃO 2: Subtração')
    print('OPÇÃO 3: Multiplicação')
    print('OPÇÃO 4: Divisão')
    print('OPÇÃO 5: Sair')

    print('-------------------------------------')

    r = (input('Qual tipo de operação deseja efetuar? '))

    print('-------------------------------------')

    if r == '1':
        soma = 0
        p = float(input('Digite o primeiro valor? '))
        s = float(input('Digite o segundo valor? '))
        print('Calculando...')
        soma = p + s
        print(soma)
    
    elif r == '2':
        sub = 0
        p = float(input('Digite o primeiro valor? '))
        s = float(input('Digite o segundo valor? '))
        print('Calculando...')       
        sub = p - s
        print(sub)

    elif r == '3':
        multi = 0
        p = float(input('Digite o primeiro valor? '))
        s = float(input('Digite o segundo valor? '))
        print('Calculando...')
        multi = p * s
        print(multi)

    elif r == '4':
        div = 0
        p = float(input('Digite o primeiro valor? '))
        s = float(input('Digite o segundo valor? '))
        print('Calculando...')
        div = p / s
        print(div)

    elif r == '5':
        print('SAINDO...')

    else:
        print('Resposta Inválida!')
    
    

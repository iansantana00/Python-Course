def teste_args_kwargs(arg1,	arg2, arg3):
    print("arg1:	",	arg1)
    print("arg2:	",	arg2)
    print("arg3:	",	arg3)


args = (1, 2, 'três')
teste_args_kwargs(*args)

ian = {'arg1': 'Barba', 'arg2': 21, 'arg3': 175}
teste_args_kwargs(**ian)

arquivo = open('palavras.txt', 'w')
arquivo.write('Ian\n')
arquivo.write('Santana\n')
arquivo.write('Reis')
arquivo.close()

with open('teste.txt') as arquivo:
    for linha in arquivo:
        print(linha)
    arquivo.seek(0)
    arquivo.read()

with open('teste.txt') as arquivo:
    arquivo.read()

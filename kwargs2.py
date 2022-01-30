"""
CONTINUAÇÃO kwargs.py

# Nas nossas funções, podemos ter (NESTA ORDEM):

- Parâmetros obrigatórios;
- *args
- Parâmetros default (não obrigatório);
- **kwargs
"""

#                 Par. Obr.          Par. default
def minha_funcao(idade, nome, *args, solteiro=False, **kawargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else: 
        print('Casado')
    print(kawargs)

minha_funcao(8, 'julia')
minha_funcao(18, 'Felicity', 4, 5, 6, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

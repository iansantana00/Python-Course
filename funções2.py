"""
CONTINUAÇÃO funções.py ...

Em Python, a forma geral de difinir uma funções é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline (Snake Case);

parametros_de_entrada -> Opcionais, se houver mais de um, devem ser separados por vírgula;

bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utilizamos a palavra reservada 'def' informando ao Python que estamos definindo uma função.
Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado em Python para definir blocos.
"""

# Definindo a primeira função

# Definição
def diz_oi():
    print('Oi!')

"""
OBS:

1 - Veja que, dentro das nossas funções podemos utilizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada; 
"""

# Utilizando funções

# Chamada de execução
diz_oi()

"""
ATENÇÃO: 

Nunca esqueça de utilizar o parênteses ao executar uma função.

Exemplo:

# Errado!
diz_oi

# Certo!
diz_oi()
"""

# Exemplo 2

def cantar_parabens():
    print('Parabens pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')

# for n in range(4):
#   cantar_parabens()

# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar está função através da variável

cantar = cantar_parabens

cantar()